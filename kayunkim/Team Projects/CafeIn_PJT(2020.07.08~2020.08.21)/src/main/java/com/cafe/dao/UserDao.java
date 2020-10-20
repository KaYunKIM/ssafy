package com.cafe.dao;

import java.util.List;

import com.cafe.dto.UserDto;

public interface UserDao {
	public List<String> search(String keyword);
	public int insert(UserDto user);
	public int delete(String id);
	public int update(UserDto user);
	public UserDto select(String id);
	public List<UserDto> selectAll();
	public UserDto findpassword(UserDto user);
	public int updateRefreshToken(UserDto user);
}
