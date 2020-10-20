package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.PostDao;
import com.cafe.dto.PostDto;



@Service
public class PostServiceImpl implements PostService {

	@Autowired
	private PostDao dao;
	
	@Override
	public PostDto select(int pno) {
		return dao.select(pno);
	}
	
	@Override
	public List<PostDto> selectAll(int page) {
		return dao.selectAll(page);
	}
	
	@Override
	public int countByUser(String uid) {
		return dao.countByUser(uid);
	}

	@Override
	public List<PostDto> selectAllByUser(int page, String uid) {
		return dao.selectAllByUser(page,uid);
	}

	@Override
	public List<PostDto> selectAllByCafe(int page, int cafeno) {
		return dao.selectAllByCafe(page,cafeno);
	}
	
	@Override
	public int insert(PostDto post) {
		return dao.insert(post);
	}

	@Override
	public int update(PostDto post) {
		return dao.update(post);
	}

	@Override
	public int delete(int pno) {
		return dao.delete(pno);
	}
	

	

}
