package com.cafe.service;

import java.util.List;

import com.cafe.dto.CafeDto;
import com.cafe.dto.UserDto;


public interface RecommendService {
	public List<CafeDto> recommendByType(String type);
	public List<CafeDto> recommendAllByType(String type, int page);
	public int setUserType(UserDto user);
	public List<Integer> selectCafeLiked(String uid);
	public List<String> selectUserLiked(int cafeno);
	public List<Integer> selectCafeStamped(String uid);
	public List<String> selectUserStamped(int cafeno);
}
