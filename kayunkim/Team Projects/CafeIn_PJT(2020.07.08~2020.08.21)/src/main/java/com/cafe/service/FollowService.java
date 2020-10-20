package com.cafe.service;

import java.util.List;

import com.cafe.dto.FollowDto;
import com.cafe.dto.LikeDto;

public interface FollowService {
	int check(FollowDto follow);
	public int countFollower(String followingid);
	public int countFollowing(String uid);
	public List<String> selectFollower(String followingid);
	public List<String> selectFollowing(String uid);
	public int insert(FollowDto follow);
	public int delete(FollowDto follow);
}
