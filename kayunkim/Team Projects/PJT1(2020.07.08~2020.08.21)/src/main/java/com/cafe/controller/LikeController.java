package com.cafe.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cafe.annotation.LoginRequired;
import com.cafe.dto.CafeDto;
import com.cafe.dto.LikeDto;
import com.cafe.service.CafeService;
import com.cafe.service.LikeService;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.Authorization;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/like")
public class LikeController {
	@Autowired
	private LikeService service;

	@Autowired
	private CafeService caService;

	@ApiOperation(value = "좋아요 수")
	@GetMapping("/{cafeno}")
	public int count(@PathVariable Integer cafeno) {
		System.out.println("count likes");
		return service.count(cafeno);
	}

	@ApiOperation(value = "이전에 좋아요 눌렀는지 체크(눌렀으면 1,안눌렀으면 0)", authorizations = { @Authorization(value = "jwt_token") })
	@GetMapping("/check/{cafeno}/{uid}")
	@LoginRequired
	public int select(@PathVariable Integer cafeno, @PathVariable String uid) {
		LikeDto like = new LikeDto();
		like.setCafeno(cafeno);
		like.setUid(uid);
		System.out.println(uid);
		return service.selectByUser(like);
	}

	@ApiOperation(value = "좋아요 추가", authorizations = { @Authorization(value = "jwt_token") })
	@PostMapping
	@LoginRequired
	public String insert(@RequestBody LikeDto like) {
		System.out.println("insert like");
		if (service.insert(like) > 0) {
			CafeDto cafe = caService.select(like.getCafeno());
			cafe.setLike_count(cafe.getLike_count() + 1);
			cafe.setRecent_like(like.getLno());
			service.update(cafe);
			return "Success";
		}
		return "Failure";
	}

	@ApiOperation(value = "좋아요 삭제", authorizations = { @Authorization(value = "jwt_token") })
	@DeleteMapping("/delete/{cafeno}/{uid}")
	@LoginRequired
	public String delete(@PathVariable Integer cafeno, @PathVariable String uid) {
		System.out.println("delete like");
		LikeDto like = new LikeDto();
		like.setCafeno(cafeno);
		like.setUid(uid);
		if (service.delete(like) > 0) {
			CafeDto cafe = caService.select(like.getCafeno());
			cafe.setLike_count(cafe.getLike_count() - 1);
			Integer max = service.getMaxLike(cafeno);
			if (max == null) {
				cafe.setRecent_like(0);
			} else {
				cafe.setRecent_like(max);
			}
			service.update(cafe);

			return "Success";
		}
		return "Failure";
	}

	@ApiOperation(value = "유저가 좋아요 누른 카페리스트")
	@GetMapping("/list/{uid}")
	public List<CafeDto> selectCafe(@PathVariable String uid) {
		System.out.println("cafe list liked by user");
		System.out.println(uid);
		List<CafeDto> cafeList = service.selectCafe(uid);
		return cafeList;
	}

}
