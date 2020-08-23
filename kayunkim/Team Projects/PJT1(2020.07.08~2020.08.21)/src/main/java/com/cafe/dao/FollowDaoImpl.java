package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.FollowDto;
import com.cafe.dto.LikeDto;

@Repository
public class FollowDaoImpl implements FollowDao {

	@Autowired
	private SqlSession session;
	
	@Override
	public int check(FollowDto follow) {
		return session.selectOne("follow.check", follow);
	}
	
	@Override
	public int countFollower(String followingid) {
		return session.selectOne("follow.countFollower",followingid);
	}

	@Override
	public int countFollowing(String uid) {
		return session.selectOne("follow.countFollowing", uid);
	}

	@Override
	public List<String> selectFollower(String followingid) {
		return session.selectList("follow.selectFollower", followingid);
	}

	@Override
	public List<String> selectFollowing(String uid) {
		return session.selectList("follow.selectFollowing", uid);
	}

	@Override
	public int insert(FollowDto follow) {
		return session.insert("follow.insert", follow);
	}

	@Override
	public int delete(FollowDto follow) {
		return session.delete("follow.delete", follow);
	}

}
