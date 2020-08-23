package com.cafe.controller;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.LinkedList;
import java.util.List;
import org.apache.commons.io.IOUtils;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.cafe.annotation.LoginRequired;
import com.cafe.dto.CafeDto;
import com.cafe.dto.GeoDto;
import com.cafe.service.CafeService;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.Authorization;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/cafe")
//http://localhost:8080/swagger-ui.html
public class CafeController {

	@Autowired
	private CafeService service;

	// 카페검색
	@ApiOperation(value = "카페 검색해서 리스트 가져오기")
	@GetMapping("/search/{keyword}")
	public List<CafeDto> search(@PathVariable String keyword) {
		System.out.println("search cafe list");
		List<CafeDto> cafeList = service.search(keyword);
		return cafeList;
	}

	@ApiOperation(value = "카페 사진 가져오기")
	@GetMapping(value = "/get/image/{cafeno}",
			produces = MediaType.IMAGE_JPEG_VALUE)
	public @ResponseBody byte[] getImage(@PathVariable Integer cafeno) {
		CafeDto cafe = service.select(cafeno);
		String target = cafe.getThumb();
//		target = "/picture/kum.jpg";
		System.out.println(target);
		FileInputStream in;
		try {
			in = new FileInputStream(target);
			return IOUtils.toByteArray(in);
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			System.out.println("i cant find file");
			e1.printStackTrace();
			return null;
		}
	}
	@ApiOperation(value = "카페 정보 가져오기")
	@GetMapping("/{cafeno}")
	public CafeDto select(@PathVariable Integer cafeno) {
		CafeDto cafe = service.select(cafeno);
		System.out.println(cafe);
		return cafe;
	}

	
	@ApiOperation(value = "카페 전체 리스트")//infinite scroll
	@GetMapping("/list/{page}")
	public List<CafeDto> selectAllByPage(@PathVariable Integer page) {
		System.out.println(page);
		List<CafeDto> cafeList = service.selectAllByPage(page);
		return cafeList;
	}
	
	
	public List<CafeDto> selectAllByLikeCount() {//좋아요 많은순 카페리스트 가져오기
		List<CafeDto> cafeList = service.selectAllByLikeCount();
		return cafeList;
	}
	
	public List<CafeDto> selectAllByStampCount() {//스탬프 많은순 카페리스트 가져오기
		List<CafeDto> cafeList = service.selectAllByStampCount();
		return cafeList;
	}
	
	public List<CafeDto> selectAllByLikeRecent() {//좋아요 많은순 카페리스트 가져오기
		List<CafeDto> cafeList = service.selectAllByLikeRecent();
		return cafeList;
	}
	
	public List<CafeDto> selectAllByStampRecent() {//스탬프 많은순 카페리스트 가져오기
		List<CafeDto> cafeList = service.selectAllByStampRecent();
		return cafeList;
	}
	
	@ApiOperation(value = "현위치 가장 가까운 카페 찾기")
	@PostMapping("/geolocation/")
	public List<CafeDto> getClosedCafe(@RequestBody GeoDto geo) {
		System.out.println("geolocation api entered");
		System.out.println(geo.getLat() +","+ geo.getLng());
		
		List<CafeDto> cafeList = service.selectAllAll(geo); // mybatis 에서 다처리함.

		return cafeList;
	}

	@ApiOperation(value = "카페 추가", authorizations = { @Authorization(value = "jwt_token") })
	@PostMapping
	@LoginRequired
	public String insert(@RequestBody CafeDto cafe) {
		int cnt = service.insert(cafe);
		System.out.println(cafe);
		if (cnt > 0) {
			return "Success";
		}
		return "Failure";
	}

	@ApiOperation(value = "카페 수정", authorizations = { @Authorization(value = "jwt_token") })
	@PutMapping
	@LoginRequired
	public String update(@RequestBody CafeDto cafe) {
		System.out.println("update");
		System.out.println(cafe);
		int cnt = service.update(cafe);
		if (cnt > 0) {
			return "Success";
		}
		return "Failure";
	}

	@ApiOperation(value = "카페 삭제", authorizations = { @Authorization(value = "jwt_token") })
	@DeleteMapping("/delete/{cafeno}")
	@LoginRequired
	public String delete(@PathVariable Integer cafeno) {
		System.out.println("delete");
		int cnt = service.delete(cafeno);
		if (cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
	
	

}
