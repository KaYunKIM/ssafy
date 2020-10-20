package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.RowBounds;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.CafeDto;
import com.cafe.dto.GeoDto;



@Repository
public class CafeDaoImpl implements CafeDao {

	@Autowired
	private SqlSession session;
	
	@Override
	public List<CafeDto> search(String keyword) {
		return session.selectList("cafe.search",keyword);
	}
	
	@Override
	public CafeDto select(int cafeno) {
		return session.selectOne("cafe.select", cafeno);
	}
	
	@Override
	public List<CafeDto> selectAllByPage(int page) {//infinite scroll
		int n = 20; //한번에 보여줄 데이터 갯수
		RowBounds bound = new RowBounds((page - 1) * n, n);
		return session.selectList("cafe.selectAllByPage", null, bound);
	}
	@Override
	public List<CafeDto> selectAllByLikeCount(){
		return session.selectList("cafe.selectAllByLikeCount");
	}
	
	@Override
	public List<CafeDto> selectAllByStampCount(){
		return session.selectList("cafe.selectAllByStampCount");
	}
	
	@Override
	public List<CafeDto> selectAllByLikeRecent(){
		return session.selectList("cafe.selectAllByLikeRecent");
	}
	
	@Override
	public List<CafeDto> selectAllByStampRecent(){
		return session.selectList("cafe.selectAllByStampRecent");
	}
	
	@Override
	public List<CafeDto> selectAllAll(GeoDto geo){
		return session.selectList("cafe.selectAllAll",geo);
	}
	@Override
	public int insert(CafeDto cafe) {
		return session.insert("cafe.insert", cafe);
	}

	@Override
	public int update(CafeDto cafe) {
		return session.update("cafe.update", cafe);
	}

	@Override
	public int delete(int cafeno) {
		return session.delete("cafe.delete", cafeno);
	}

	

}
