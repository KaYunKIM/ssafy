package com.cafe.dto;

public class GeoDto {
	private double lat;
	private double lng;
	public double getLat() {
		return lat;
	}
	public void setLat(double lat) {
		this.lat = lat;
	}
	public double getLng() {
		return lng;
	}
	public void setLng(double lng) {
		this.lng = lng;
	}
	@Override
	public String toString() {
		return "GeoDto [lat=" + lat + ", lng=" + lng + "]";
	}
	public GeoDto(double lat, double lng) {
		super();
		this.lat = lat;
		this.lng = lng;
	}
	public GeoDto() {
		super();
		// TODO Auto-generated constructor stub
	}
	
}
