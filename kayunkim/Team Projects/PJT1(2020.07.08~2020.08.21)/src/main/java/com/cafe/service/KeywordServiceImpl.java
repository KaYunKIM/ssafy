package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.KeywordDao;
import com.cafe.dto.CafeDto;
import com.cafe.dto.KeywordDto;

@Service
public class KeywordServiceImpl implements KeywordService {

	@Autowired
	private KeywordDao dao;
	@Override
	public List<KeywordDto> selectByCafe(int cafeno) {
		return dao.selectByCafe(cafeno);
	}

	@Override
	public List<CafeDto> selectByKeyword(String keyword) {
		return dao.selectByKeyword(keyword);
	}

	@Override
	public int insert(KeywordDto keyword) {
		return dao.insert(keyword);
	}

	@Override
	public int update(KeywordDto keyword) {
		return dao.update(keyword);
	}

	@Override
	public int delete(int idx) {
		return dao.delete(idx);
	}

}
