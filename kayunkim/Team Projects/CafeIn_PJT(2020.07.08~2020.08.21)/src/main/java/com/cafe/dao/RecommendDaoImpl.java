package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.RowBounds;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.CafeDto;
import com.cafe.dto.UserDto;

@Repository
public class RecommendDaoImpl implements RecommendDao {

	@Autowired
	private SqlSession session;
	
	@Override
	public List<CafeDto> recommendAllByTheme(String theme, int page) {
		int n = 10; //한번에 보여줄 데이터 갯수
		RowBounds bound = new RowBounds((page - 1) * n, n);
		return session.selectList("recommend.recommendAllByTheme", theme, bound);
	}

	
	@Override
	public List<CafeDto> recommendByType(String type) {
		return session.selectList("recommend.recommendByType", type);
	}

	@Override
	public List<CafeDto> recommendAllByType(String type, int page) {
		int n = 10; //한번에 보여줄 데이터 갯수
		RowBounds bound = new RowBounds((page - 1) * n, n);
		return session.selectList("recommend.recommendAllByType", type, bound);
	}

	@Override
	public int setUserType(UserDto user) {
		return session.update("recommend.setUserType", user);
	}
	
	@Override
	public List<Integer> selectCafeLiked(String uid) {
		return session.selectList("recommend.selectCafeLiked", uid);
	}

	@Override
	public List<String> selectUserLiked(int cafeno) {
		return session.selectList("recommend.selectUserLiked", cafeno);
	}

	@Override
	public List<Integer> selectCafeStamped(String uid) {
		return session.selectList("recommend.selectCafeStamped", uid);
	}

	@Override
	public List<String> selectUserStamped(int cafeno) {
		return session.selectList("recommend.selectUserStamped", cafeno);
	}

	


}
