package com.cafe.service;

import java.util.List;

import com.cafe.dto.CafeDto;
import com.cafe.dto.GeoDto;

public interface CafeService {

	public List<CafeDto> search(String keyword);

	public CafeDto select(int cafeno);

	public List<CafeDto> selectAllByPage(int page);// infinite scroll

	public List<CafeDto> selectAllByLikeCount();

	public List<CafeDto> selectAllByStampCount();

	public List<CafeDto> selectAllByLikeRecent();

	public List<CafeDto> selectAllByStampRecent();
	
	public List<CafeDto> selectAllAll(GeoDto geo); // this is used for finding geo

	public int insert(CafeDto cafe);

	public int update(CafeDto cafe);

	public int delete(int cafeno);

}
