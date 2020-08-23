package com.cafe.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cafe.dao.MenuDao;
import com.cafe.dto.MenuDto;

@Service
public class MenuServiceImpl implements MenuService {

	@Autowired
	private MenuDao dao;
	
	@Override
	public List<MenuDto> selectAll(int cafeno) {
		return dao.selectAll(cafeno);
	}

	@Override
	public int insert(MenuDto menu) {
		return dao.insert(menu);
	}

	@Override
	public int update(MenuDto menu) {
		return dao.update(menu);
	}

	@Override
	public int delete(int mno) {
		return dao.delete(mno);
	}

}
