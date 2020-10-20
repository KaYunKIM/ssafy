package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.UserDto;
import com.mysql.cj.Session;

@Repository
public class UserDaoImpl implements UserDao {

	@Autowired
	SqlSession session;
	
	@Override
	public List<String> search(String keyword) {
		return session.selectList("user.search", keyword);
	}
	
	@Override
	public int insert(UserDto user) {
		return session.insert("user.insert", user);
	}

	@Override
	public int delete(String id) {
		return session.delete("user.delete", id);
	}

	@Override
	public int update(UserDto user) {
		return session.update("user.update", user);
	}

	@Override
	public UserDto select(String id) {
		return session.selectOne("user.select", id);
	}

	@Override
	public List<UserDto> selectAll() {
		return session.selectList("user.selectAll");
	}

	@Override
	public UserDto findpassword(UserDto user) {
		return session.selectOne("user.findpassword", user);
	}

	
	@Override
	public int updateRefreshToken(UserDto user){
		return session.update("user.update_refreshToken", user);
	}
}
