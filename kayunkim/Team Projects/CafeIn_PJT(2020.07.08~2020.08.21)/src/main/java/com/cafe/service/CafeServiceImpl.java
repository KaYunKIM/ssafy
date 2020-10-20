package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.CafeDao;
import com.cafe.dto.CafeDto;
import com.cafe.dto.GeoDto;


@Service
public class CafeServiceImpl implements CafeService {

	@Autowired
	private CafeDao dao;
	
	@Override
	public List<CafeDto> search(String keyword) {
		return dao.search(keyword);
	}
	
	@Override
	public CafeDto select(int cafeno) {
		return dao.select(cafeno);
	}

	@Override
	public List<CafeDto> selectAllByPage(int page) {
		return dao.selectAllByPage(page);
	}
	
	@Override
	public List<CafeDto> selectAllByLikeCount() {
		return dao.selectAllByLikeCount();
	}
	
	@Override
	public List<CafeDto> selectAllByStampCount() {
		return dao.selectAllByStampCount();
	}
	
	@Override
	public List<CafeDto> selectAllByLikeRecent() {
		return dao.selectAllByLikeRecent();
	}
	
	@Override
	public List<CafeDto> selectAllByStampRecent() {
		return dao.selectAllByStampRecent();
	}
	
	@Override
	public List<CafeDto> selectAllAll(GeoDto geo){
		return dao.selectAllAll(geo);
	}
	@Override
	public int insert(CafeDto cafe) {
		return dao.insert(cafe);
	}

	@Override
	public int update(CafeDto cafe) {
		return dao.update(cafe);
	}

	@Override
	public int delete(int cafeno) {
		return dao.delete(cafeno);
	}

	

}
