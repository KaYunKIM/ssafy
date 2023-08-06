package com.cafe.service;

import java.util.List;

import com.cafe.dto.CafeDto;
import com.cafe.dto.KeywordDto;

public interface KeywordService {

	public List<KeywordDto> selectByCafe(int cafeno);
	public List<CafeDto> selectByKeyword(String keyword);
	public int insert(KeywordDto keyword);
	public int update(KeywordDto keyword);
	public int delete(int idx);
}
