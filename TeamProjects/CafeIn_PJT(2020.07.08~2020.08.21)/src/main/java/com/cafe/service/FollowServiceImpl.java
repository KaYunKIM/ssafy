package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.FollowDao;
import com.cafe.dto.FollowDto;
import com.cafe.dto.LikeDto;

@Service
public class FollowServiceImpl implements FollowService {

	@Autowired
	private FollowDao dao;
	
	@Override
	public int check(FollowDto follow) {
		return dao.check(follow);
	}
	
	@Override
	public int countFollower(String followingid) {
		return dao.countFollower(followingid);
	}

	@Override
	public int countFollowing(String uid) {
		return dao.countFollowing(uid);
	}

	@Override
	public List<String> selectFollower(String followingid) {
		return dao.selectFollower(followingid);
	}

	@Override
	public List<String> selectFollowing(String uid) {
		return dao.selectFollowing(uid);
	}

	@Override
	public int insert(FollowDto follow) {
		return dao.insert(follow);
	}

	@Override
	public int delete(FollowDto follow) {
		return dao.delete(follow);
	}

}
