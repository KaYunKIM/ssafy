package com.cafe.service;

import java.util.List;

import com.cafe.dto.MenuDto;

public interface MenuService {
	public List<MenuDto> selectAll(int cafeno);
	public int insert(MenuDto menu);
	public int update(MenuDto menu);
	public int delete(int mno);
}
