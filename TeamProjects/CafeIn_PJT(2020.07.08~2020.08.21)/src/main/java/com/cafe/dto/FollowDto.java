package com.cafe.dto;

public class FollowDto {
	private int fno;
	private String uid;
	private String followingid;
	
	public int getFno() {
		return fno;
	}
	public void setFno(int fno) {
		this.fno = fno;
	}
	public String getUid() {
		return uid;
	}
	public void setUid(String uid) {
		this.uid = uid;
	}
	public String getFollowingid() {
		return followingid;
	}
	public void setFollowingid(String followingid) {
		this.followingid = followingid;
	}
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("FollowDto [fno=").append(fno).append(", uid=").append(uid).append(", followingid=")
				.append(followingid).append("]");
		return builder.toString();
	}
	
	
}
