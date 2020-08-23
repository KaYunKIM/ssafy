package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.RowBounds;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.PostDto;



@Repository
public class PostDaoImpl implements PostDao {

	@Autowired
	private SqlSession session;
	
	@Override
	public PostDto select(int pno) {
		return session.selectOne("post.select", pno);
	}
	
	@Override
	public List<PostDto> selectAll(int page) {
		return session.selectList("post.selectAll",page);
	}

	
	@Override
	public int countByUser(String uid) {
		return session.selectOne("post.countByUser", uid);
	}
	
	@Override
	public List<PostDto> selectAllByUser(int page, String uid) {
		int n = 10;
		RowBounds bound = new RowBounds((page - 1) * n, n);
		return session.selectList("post.selectAllByUser", uid, bound);
	}
	@Override
	public List<PostDto> selectAllByCafe(int page, int cafeno) {
		int n = 10;
		RowBounds bound = new RowBounds((page - 1) * n, n);
		return session.selectList("post.selectAllByCafe", cafeno, bound);
	}

	@Override
	public int insert(PostDto post) {
		return session.insert("post.insert", post);
	}

	@Override
	public int update(PostDto post) {
		return session.update("post.update", post);
	}

	@Override
	public int delete(int pno) {
		return session.delete("post.delete", pno);
	}

	
	

}
