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
import com.cafe.dto.FollowDto;
import com.cafe.dto.LikeDto;
import com.cafe.service.FollowService;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.Authorization;



@CrossOrigin("*")
@RestController
@RequestMapping("/api/follow")
public class FollowController {
	@Autowired
	private FollowService service;
	
	@ApiOperation(value = "이전에 팔로우 눌렀는지 체크(눌렀으면 1,안눌렀으면 0)", authorizations = { @Authorization(value="jwt_token") })
	@GetMapping("/check/{uid}/{followingid}")
	@LoginRequired
	public int check(@PathVariable String uid, @PathVariable String followingid) {
		FollowDto follow = new FollowDto();
		follow.setUid(uid);
		follow.setFollowingid(followingid);
		return service.check(follow);
	}
	
	@ApiOperation(value = "팔로워 수")
	@GetMapping("/count/follower/{followingid}")
	public int countFollower(@PathVariable String followingid) {
		System.out.println("count follower");
		return service.countFollower(followingid);
	}
	
	@ApiOperation(value = "팔로잉 수")
	@GetMapping("/count/following/{uid}")
	public int countFollowing(@PathVariable String uid) {
		System.out.println("count following");
		return service.countFollowing(uid);
	}
	
	@ApiOperation(value = "팔로워 리스트")
	@GetMapping("/list/follower/{followingid}")
	public List<String> selectFollower(@PathVariable String followingid) {
		System.out.println("select follower");
		System.out.println("followingid: " + followingid);
		List<String> follwerList = service.selectFollower(followingid);
		for(String s: follwerList) {
			System.out.println(s);
		}
		return follwerList;
	}
	
	@ApiOperation(value = "팔로잉 리스트")
	@GetMapping("/list/following/{uid}")
	public List<String> selectFollowing(@PathVariable String uid) {
		System.out.println("select following");
		System.out.println("uid: " + uid);
		List<String> follwingList = service.selectFollowing(uid);
		for(String s: follwingList) {
			System.out.println(s);
		}
		return follwingList;
	}
	
	@ApiOperation(value = "팔로우 추가", authorizations = { @Authorization(value="jwt_token") })
	@PostMapping
	@LoginRequired
	public String insert(@RequestBody FollowDto follow) {
		System.out.println("insert follow");
		if(service.insert(follow)>0) {
			return "Success";
		}
		return "Failure";
	}
	
	@ApiOperation(value = "팔로우 삭제", authorizations = { @Authorization(value="jwt_token") })
	@DeleteMapping("/delete/{uid}/{followingid}")
	@LoginRequired
	public String delete(@PathVariable String uid, @PathVariable String followingid) {
		System.out.println("delete follow");
		FollowDto follow = new FollowDto();
		follow.setUid(uid);
		follow.setFollowingid(followingid);
		if(service.delete(follow)>0) {
			return "Success";
		}
		return "Failure";
	}
	
}
