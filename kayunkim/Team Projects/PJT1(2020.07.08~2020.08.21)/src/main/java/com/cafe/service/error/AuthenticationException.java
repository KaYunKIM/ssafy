package com.cafe.service.error;

public class AuthenticationException extends RuntimeException{
   	private static final long serialVersionUID = 1L;

	public AuthenticationException() {
		super();
	}
	public AuthenticationException(String orgRequestUrl) {
		super(orgRequestUrl);
	} 
}