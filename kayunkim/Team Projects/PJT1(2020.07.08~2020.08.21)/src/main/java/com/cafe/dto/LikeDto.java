package com.cafe.dto;

public class LikeDto {

	private int lno;

	private int cafeno;

	private String uid;

	public int getLno() {
		return lno;
	}

	public void setLno(int lno) {
		this.lno = lno;
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
		builder.append("LikeDto [lno=").append(lno).append(", cafeno=").append(cafeno).append(", uid=").append(uid)
				.append("]");
		return builder.toString();
	}

	
}
