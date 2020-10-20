package com.cafe.dto;

public class KeywordDto {
	private int idx;
	private int cafeno;
	private int keyno;
	private String keyword;
	
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public int getCafeno() {
		return cafeno;
	}
	public void setCafeno(int cafeno) {
		this.cafeno = cafeno;
	}
	public int getKeyno() {
		return keyno;
	}
	public void setKeyno(int keyno) {
		this.keyno = keyno;
	}
	public String getKeyword() {
		return keyword;
	}
	public void setKeyword(String keyword) {
		this.keyword = keyword;
	}
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("KeywordDto [idx=").append(idx).append(", cafeno=").append(cafeno).append(", keyno=")
				.append(keyno).append(", keyword=").append(keyword).append("]");
		return builder.toString();
	}
	
	
}
