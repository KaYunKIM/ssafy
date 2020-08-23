package com.cafe.service;

import java.util.List;

import com.cafe.dto.CommentDto;



public interface CommentService {
	
	public CommentDto select(int cno);
	
	public List<CommentDto> selectAll(int pno, int page);
	
	public int insert(CommentDto comment);
	
	public int update(CommentDto comment);
	
	public int delete(int cno);

	int maxCno();
}
