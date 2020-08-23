package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.RowBounds;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.CommentDto;



@Repository
public class CommentDaoImpl implements CommentDao {

	@Autowired
	private SqlSession session;

	@Override
	public int maxCno() {
		return session.selectOne("comment.selectMax");
	}
	
	@Override
	public CommentDto select(int cno) {
		return session.selectOne("comment.select", cno);
	}

	@Override
	public List<CommentDto> selectAll(int pno, int page) {
		int n = 100;
		RowBounds bound = new RowBounds((page - 1) * n, n);
		return session.selectList("comment.selectAll", pno, bound);
	}

	@Override
	public int insert(CommentDto comment) {
		return session.insert("comment.insert", comment);
	}

	@Override
	public int update(CommentDto comment) {
		return session.update("comment.update", comment);
	}

	@Override
	public int delete(int cno) {
		return session.delete("comment.delete", cno);
	}
	
}
