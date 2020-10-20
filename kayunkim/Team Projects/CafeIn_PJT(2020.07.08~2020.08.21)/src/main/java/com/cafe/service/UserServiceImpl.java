package com.cafe.service;

import java.util.List;

import org.mindrot.jbcrypt.BCrypt;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.UserDao;
import com.cafe.dto.UserDto;


@Service
public class UserServiceImpl implements UserService {

	private static final Logger logger = LoggerFactory.getLogger(UserServiceImpl.class);
	
	@Autowired
	private UserDao userDao;
	
	@Override
	public UserDao getUserDao() {
		return userDao;
	}

	@Override
	public List<String> search(String keyword) {
		return userDao.search(keyword);
	}
	@Override
	public UserDto select(String id) {
		return userDao.select(id);
	}

	@Override
	public UserDto login(String id, String pw) {
		UserDto user = userDao.select(id);
		if(user != null && checkPass(pw,user.getPassword())){
			return user;
		}else {
			return null;
		}
	}

	@Override
	public int join(UserDto user) {
		String origin = user.getPassword();
		if(origin == null) {
			return -1;
		}else {
			String hashed = hashPassword(origin);
			System.out.println(hashed);
			user.setPassword(hashed);
		}
		int result = userDao.insert(user);
		UserDto selected = userDao.select(user.getId());
		logger.trace("조회 결과:{}", selected);
		return result;
	}

	@Override
	public int delete(String id) {
		return userDao.delete(id);
	}

	@Override
	public int update(UserDto user) {
		String origin = user.getPassword();
		if(origin == null) { 
			return -1; 
		}else {
			String hashed = hashPassword(origin);
			System.out.println(hashed);
			user.setPassword(hashed);
		}
		return userDao.update(user);
	}

	@Override
	public List<UserDto> selectAll() {
		return userDao.selectAll();
	}

	@Override
	public UserDto findpassword(UserDto user) {
		UserDto result = userDao.findpassword(user);
		if(result != null && result.getPassword() != null) {
			return result;
		}else {
			return null;
		}
	}

	
	private String hashPassword(String plainTextPassword) {  // 일반적인 String 패스워드 암호화
		return BCrypt.hashpw(plainTextPassword, BCrypt.gensalt()); 
	}

	private Boolean checkPass(String plainPassword, String hasedPassword) { // 암호화된 패스워드와 원문 매칭 
		if (BCrypt.checkpw(plainPassword, hasedPassword)) {  // 매칭이 됬다면? 
			return true;
		}
		return false; // 아니면 false 리턴
	}

	@Override
	public int updateRefreshToken(UserDto user){
		return userDao.updateRefreshToken(user);
	}
}
