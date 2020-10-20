package com.cafe.controller;

import java.util.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cafe.annotation.LoginRequired;
import com.cafe.dto.MenuDto;
import com.cafe.dto.PostDto;
import com.cafe.service.MenuService;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.Authorization;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/menu")
public class MenuController {

	@Autowired
	private MenuService service;
	
	@ApiOperation(value = "메뉴 리스트")
	@GetMapping("/list/{cafeno}")
	public List<MenuDto> selectAll(@PathVariable Integer cafeno){
		System.out.println("selectAll");
		return service.selectAll(cafeno);
	}
	
	@ApiOperation(value = "메뉴 추가", authorizations = { @Authorization(value="jwt_token") })
	@PostMapping
	@LoginRequired
	public String insert(@RequestBody MenuDto menu) {
		System.out.println("insert");
		int cnt = service.insert(menu);
		System.out.println(menu);
		if(cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
	
	@ApiOperation(value = "메뉴 수정", authorizations = { @Authorization(value="jwt_token") })
	@PutMapping
	@LoginRequired
	public String update(@RequestBody MenuDto menu) {
		System.out.println("update");
		System.out.println(menu);
		int cnt = service.update(menu);
		if(cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
	
	@ApiOperation(value = "메뉴 삭제", authorizations = { @Authorization(value="jwt_token") })
	@DeleteMapping("/delete/{mno}")
	@LoginRequired
	public String delete(@PathVariable Integer mno) {
		System.out.println("delete");
		int cnt = service.delete(mno);
		if(cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
}
