package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.CafeDto;
import com.cafe.dto.LikeDto;



@Repository
public class LikeDaoImpl implements LikeDao{

	@Autowired
	private SqlSession session;
	
	@Override
	public int count(int cafeno) {
		return session.selectOne("like.count", cafeno);
	}

	@Override
	public int insert(LikeDto like) {
		return session.insert("like.insert", like);
	}

	@Override
	public int delete(LikeDto like) {
		return session.delete("like.delete", like);
	}
	
	@Override
	public int selectByUser(LikeDto user) {
		return session.selectOne("like.selectByUser", user);
	}

	@Override
	public List<CafeDto> selectCafe(String uid) {
		return session.selectList("like.selectCafe", uid);
	}

	@Override
	public void update(CafeDto cafe) {
		session.update("like.update", cafe);
	}

	@Override
	public Integer getMaxLike(int cafeno) {
		return session.selectOne("like.getMaxLike",cafeno);
	}


	

	
}
