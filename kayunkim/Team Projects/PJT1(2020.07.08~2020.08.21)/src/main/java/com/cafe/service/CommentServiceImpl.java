package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.CommentDao;
import com.cafe.dto.CommentDto;



@Service
public class CommentServiceImpl implements CommentService {

	@Autowired
	private CommentDao dao;
	
	@Override
	public int maxCno() {
		return dao.maxCno();
	}
	
	@Override
	public CommentDto select(int cno) {
		return dao.select(cno);
	}

	@Override
	public List<CommentDto> selectAll(int pno, int page) {
		return dao.selectAll(pno, page);
	}

	@Override
	public int insert(CommentDto comment) {
		return dao.insert(comment);
	}

	@Override
	public int update(CommentDto comment) {
		return dao.update(comment);
	}

	@Override
	public int delete(int cno) {
		return dao.delete(cno);
	}

	

}
