package com.cafe.dto;

public class UserDto {
	private String id;     
	private String password;    
	private String name;
	private String gender;
	private String phone;  
	private String birth;  
	private String survey; 
	private String auth;
	private String refreshToken;

	public String getRefreshToken(){
		return refreshToken;
	}

	public void setRefreshToken(String refreshToken){
		this.refreshToken = refreshToken;
	}

	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getBirth() {
		return birth;
	}
	public void setBirth(String birth) {
		this.birth = birth;
	}
	public String getSurvey() {
		return survey;
	}
	public void setSurvey(String survey) {
		this.survey = survey;
	}
	public String getAuth() {
		return auth;
	}
	public void setAuth(String auth) {
		this.auth = auth;
	}
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("UserDto [id=").append(id).append(", password=").append(password).append(", name=").append(name)
				.append(", gender=").append(gender).append(", phone=").append(phone).append(", birth=").append(birth)
				.append(", survey=").append(survey).append(", auth=").append(auth).append("]");
		return builder.toString();
	}
	
	  
	  
}
