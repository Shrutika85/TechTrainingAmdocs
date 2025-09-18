import csv
import pymysql

# 🔌 Connect to MySQL
try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="organization"
    )
    print("Connected successfully!")
    cursor = conn.cursor()
except pymysql.MySQLError as err:
    print(" Connection failed:", err)
    exit()


def show_payroll():
    cursor.execute("SELECT * FROM payroll")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Basic: {row[3]}, Allowances: {row[4]}, Deductions: {row[5]}, Net Pay: {row[6]}")


def insert_payroll():
    name = input("Enter name: ")

    department = input("Enter department: ")
    basic_salary = float(input("Enter basic salary: "))
    allowances = float(input("Enter allowances: "))
    deductions = float(input("Enter deductions: "))
    net_pay = basic_salary + allowances - deductions
    cursor.execute(
        "INSERT INTO payroll (name, department, basic_salary, allowances, deductions, net_pay) VALUES (%s, %s, %s, %s, %s, %s)",
        (name, department, basic_salary, allowances, deductions, net_pay)
    )
    conn.commit()
    print("Payroll record added.")


def update_payroll():
    emp_id = int(input("Enter payroll ID to update: "))
    name = input("Enter new name: ")
    department = input("Enter new department: ")
    basic_salary = float(input("Enter new basic salary: "))
    allowances = float(input("Enter new allowances: "))
    deductions = float(input("Enter new deductions: "))
    net_pay = basic_salary + allowances - deductions
    cursor.execute(
        "UPDATE payroll SET name=%s, department=%s, basic_salary=%s, allowances=%s, deductions=%s, net_pay=%s WHERE id=%s",
        (name, department, basic_salary, allowances, deductions, net_pay, emp_id)
    )
    conn.commit()
    print(" Payroll record updated.")

def delete_payroll():
    emp_id = int(input("Enter payroll ID to delete: "))
    cursor.execute("DELETE FROM payroll WHERE id=%s", (emp_id,))
    conn.commit()
    print(" Payroll record deleted.")
def export_to_csv():
    cursor.execute("SELECT * FROM payroll")
    rows = cursor.fetchall()
    with open('payroll.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Department', 'Basic Salary', 'Allowances', 'Deductions', 'Net Pay'])
        writer.writerows(rows)
    print(" Data exported to payroll.csv")


def search_payroll_by_name():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM payroll WHERE name LIKE %s", ('%' + name + '%',))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Basic: {row[3]}, Allowances: {row[4]}, Deductions: {row[5]}, Net Pay: {row[6]}")
    else:
        print("No matching records found.")


def payroll_summary_by_department():
    cursor.execute("""
        SELECT department, COUNT(*), SUM(basic_salary), SUM(allowances), SUM(deductions), SUM(net_pay)
        FROM payroll
        GROUP BY department
    """)
    for row in cursor.fetchall():
        print(f"Dept: {row[0]}, Employees: {row[1]}, Total Basic: {row[2]}, Total Allowances: {row[3]}, Total Deductions: {row[4]}, Total Net Pay: {row[5]}")


def filter_by_salary_range():
    min_salary = float(input("Enter minimum net pay: "))
    max_salary = float(input("Enter maximum net pay: "))
    cursor.execute("SELECT * FROM payroll WHERE net_pay BETWEEN %s AND %s", (min_salary, max_salary))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Net Pay: {row[6]}")
    else:
        print("No employees found in this salary range.")


def menu():
    while True:
        print("\n MENU")
        print("1. Show Payroll")
        print("2. Insert Payroll")
        print("3. Update Payroll")
        print("4. Delete Payroll")
        print("5. Export to CSV")
        print("6. Search by Name")
        print("7. Summary by Department")
        print("8. Filter by Salary Range")
        print("9. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            show_payroll()
        elif choice == '2':
            insert_payroll()
        elif choice == '3':
            update_payroll()
        elif choice == '4':
            delete_payroll()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            search_payroll_by_name()
        elif choice == '7':
            payroll_summary_by_department()
        elif choice == '8':
            filter_by_salary_range()
        elif choice == '9':
            print(" Goodbye!")
            break
        else:
            print("Invalid choice.")


print(" Welcome to Payroll Management System")
menu()
conn.close()
