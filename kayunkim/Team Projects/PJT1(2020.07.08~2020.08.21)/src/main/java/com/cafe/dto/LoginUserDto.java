package com.cafe.dto;

public class LoginUserDto {
	private String id;
	private String pw;
	public LoginUserDto(String id, String pw) {
		super();
		this.id = id;
		this.pw = pw;
	}
	public LoginUserDto() {
		super();
		// TODO Auto-generated constructor stub
	}
	@Override
	public String toString() {
		return "LoginUserDto [id=" + id + ", pw=" + pw + "]";
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		this.pw = pw;
	}
	
}
