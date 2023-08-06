package com.cafe.dao;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.cafe.dto.MenuDto;

@Repository
public class MenuDaoImpl implements MenuDao {

	@Autowired
	private SqlSession session;
	
	@Override
	public List<MenuDto> selectAll(int cafeno) {
		return session.selectList("menu.selectAll", cafeno);
	}

	@Override
	public int insert(MenuDto menu) {
		return session.insert("menu.insert",menu);
	}

	@Override
	public int update(MenuDto menu) {
		return session.update("menu.update",menu);
	}

	@Override
	public int delete(int mno) {
		return session.delete("menu.delete",mno);
	}

}
