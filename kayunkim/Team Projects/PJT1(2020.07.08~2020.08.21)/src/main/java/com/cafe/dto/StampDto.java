package com.cafe.dto;

public class StampDto {

	private int sno;

	private int cafeno;

	private String uid;

	public int getSno() {
		return sno;
	}

	public void setSno(int sno) {
		this.sno = sno;
	}

	public int getCafeno() {
		return cafeno;
	}

	public void setCafeno(int cafeno) {
		this.cafeno = cafeno;
	}

	public String getUid() {
		return uid;
	}

	public void setUid(String uid) {
		this.uid = uid;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("StampDto [sno=").append(sno).append(", cafeno=").append(cafeno).append(", uid=").append(uid)
				.append("]");
		return builder.toString();
	}
	
}
