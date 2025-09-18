
package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication

@RestController
public class DemospringApplication {

	@GetMapping("/message")
	public String getMessage()
	{
		return "Welcome to session";
	}
	
	@GetMapping("/login")
	public String getLogin()
	{
		return "Click ok to Login";
	}
	@GetMapping("/home")
	public String getHoml()
	{
		return "Welcome to Home Page";
	}
	
	

	public static void main(String[] args) {
		SpringApplication.run(DemospringApplication.class, args);
	}

}
