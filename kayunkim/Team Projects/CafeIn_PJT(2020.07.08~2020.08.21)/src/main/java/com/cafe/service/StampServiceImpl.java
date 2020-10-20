package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.StampDao;
import com.cafe.dto.CafeDto;
import com.cafe.dto.StampDto;



@Service
public class StampServiceImpl implements StampService {

	@Autowired
	private StampDao dao;
	
	@Override
	public int count(int cafeno) {
		return dao.count(cafeno);
	}
	
	@Override
	public int insert(StampDto stamp) {
		return dao.insert(stamp);
	}

	@Override
	public int delete(StampDto stamp) {
		return dao.delete(stamp);
	}

	@Override
	public int selectByUser(StampDto user) {
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
	public Integer getMaxStamp(int cafeno) {
		return dao.getMaxStamp(cafeno);
	}
}
