package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.CafeDto;
import com.cafe.dto.KeywordDto;

@Repository
public class KeywordDaoImpl implements KeywordDao {

	@Autowired
	private SqlSession session;
	
	@Override
	public List<KeywordDto> selectByCafe(int cafeno) {
		return session.selectList("keyword.selectByCafe", cafeno);
	}

	@Override
	public List<CafeDto> selectByKeyword(String keyword) {
		return session.selectList("keyword.selectByKeyword", keyword);
	}

	@Override
	public int insert(KeywordDto keyword) {
		return session.insert("keyword.insert",keyword);
	}

	@Override
	public int update(KeywordDto keyword) {
		return session.update("keyword.update",keyword);
	}

	@Override
	public int delete(int idx) {
		return session.delete("keyword.delete",idx);
	}

}
