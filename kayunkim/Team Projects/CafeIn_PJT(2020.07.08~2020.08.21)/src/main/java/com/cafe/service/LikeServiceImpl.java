package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.LikeDao;
import com.cafe.dto.CafeDto;
import com.cafe.dto.LikeDto;



@Service
public class LikeServiceImpl implements LikeService {

	@Autowired
	private LikeDao dao;
	
	@Override
	public int count(int cafeno) {
		return dao.count(cafeno);
	}
	
	@Override
	public int insert(LikeDto like) {
		return dao.insert(like);
	}

	@Override
	public int delete(LikeDto like) {
		return dao.delete(like);
	}

	@Override
	public int selectByUser(LikeDto user) {
		return dao.selectByUser(user);
	}
	
	@Override
	public List<CafeDto> selectCafe(String uid) {
		return dao.selectCafe(uid);
	}

	@Override
	public void update(CafeDto cafe) {
		dao.update(cafe);
		
	}

	@Override
	public Integer getMaxLike(int cafeno) {
		return dao.getMaxLike(cafeno);
	}

	

	
}
