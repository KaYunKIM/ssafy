package com.cafe.dao;

import java.util.List;

import com.cafe.dto.CafeDto;
import com.cafe.dto.KeywordDto;

public interface KeywordDao {
	public List<KeywordDto> selectByCafe(int cafeno);
	public List<CafeDto> selectByKeyword(String keyword);
	public int insert(KeywordDto keyword);
	public int update(KeywordDto keyword);
	public int delete(int idx);
}
