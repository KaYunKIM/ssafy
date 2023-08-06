package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.CafeDto;
import com.cafe.dto.StampDto;



@Repository
public class StampDaoImpl implements StampDao{

	@Autowired
	private SqlSession session;
	
	@Override
	public int count(int cafeno) {
		return session.selectOne("stamp.count", cafeno);
	}

	@Override
	public int insert(StampDto stamp) {
		return session.insert("stamp.insert", stamp);
	}

	@Override
	public int delete(StampDto stamp) {
		return session.delete("stamp.delete", stamp);
	}
	
	@Override
	public int selectByUser(StampDto user) {
		return session.selectOne("stamp.selectByUser", user);
	}
	
	@Override
	public List<CafeDto> selectCafe(String uid) {
		return session.selectList("stamp.selectCafe", uid);
	}
	
	@Override
	public void update(CafeDto cafe) {
		session.update("stamp.update", cafe);
		
	}

	@Override
	public Integer getMaxStamp(int cafeno) {
		return session.selectOne("stamp.getMaxStamp",cafeno);
	}



}
