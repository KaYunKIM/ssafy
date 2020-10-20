package com.cafe.service;

import java.util.List;

import com.cafe.dao.UserDao;
import com.cafe.dto.UserDto;


public interface UserService {
	public List<String> search(String keyword);
	public UserDao getUserDao();
	public UserDto select(String id);
	public UserDto login(String id, String pw); // 로그인
	public int join(UserDto user); //가입
	public int delete(String id); // 회원 탈퇴
	public int update(UserDto user); // User 수정
	public List<UserDto> selectAll(); // 모든 User 리턴
	public UserDto findpassword(UserDto user);
	public int updateRefreshToken(UserDto user);
}
