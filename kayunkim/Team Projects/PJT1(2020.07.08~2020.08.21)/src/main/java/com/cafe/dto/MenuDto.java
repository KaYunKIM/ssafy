package com.cafe.dto;

public class MenuDto {
	private int mno;
	private int cafeno;
	private String item;
	private int price;
	public int getMno() {
		return mno;
	}
	public void setMno(int mno) {
		this.mno = mno;
	}
	public int getCafeno() {
		return cafeno;
	}
	public void setCafeno(int cafeno) {
		this.cafeno = cafeno;
	}
	public String getItem() {
		return item;
	}
	public void setItem(String item) {
		this.item = item;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("MenuDto [mno=").append(mno).append(", cafeno=").append(cafeno).append(", item=").append(item)
				.append(", price=").append(price).append("]");
		return builder.toString();
	}
	
}
