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
import com.cafe.dto.CafeDto;
import com.cafe.dto.KeywordDto;
import com.cafe.service.KeywordService;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.Authorization;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/keyword")
public class KeywordController {

	@Autowired
	private KeywordService service;
	
	@ApiOperation(value = "카페의 키워드 가져오기")
	@GetMapping("/keywords/{cafeno}")
	public List<KeywordDto> selectByCafe(@PathVariable Integer cafeno){
		System.out.println("selectByCafe");
		return service.selectByCafe(cafeno);
	}
	
	@ApiOperation(value = "키워드로 카페 리스트 가져오기")
	@GetMapping("/cafelist/{keyword}")
	public List<CafeDto> selectByKeyword(@PathVariable String keyword){
		System.out.println("selectByKeyword");
		return service.selectByKeyword(keyword);
	}
	
	@ApiOperation(value = "키워드 추가", authorizations = { @Authorization(value="jwt_token") })
	@PostMapping
	@LoginRequired
	public String insert(@RequestBody KeywordDto keyword) {
		System.out.println("insert keyword");
		int cnt = service.insert(keyword);
		System.out.println(keyword);
		if(cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
	
	@ApiOperation(value = "키워드 수정", authorizations = { @Authorization(value="jwt_token") })
	@PutMapping
	@LoginRequired
	public String update(@RequestBody KeywordDto keyword) {
		System.out.println("update keyword");
		System.out.println(keyword);
		int cnt = service.update(keyword);
		if(cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
	
	@ApiOperation(value = "키워드 삭제", authorizations = { @Authorization(value="jwt_token") })
	@DeleteMapping("/delete/{idx}")
	@LoginRequired
	public String delete(@PathVariable Integer idx) {
		System.out.println("delete keyword");
		int cnt = service.delete(idx);
		if(cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
}
