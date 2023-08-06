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

import com.cafe.dto.CafeDto;
import com.cafe.dto.UserDto;
import com.cafe.service.CafeService;
import com.cafe.service.RecommendService;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.Authorization;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/recommend")
public class RecommendController {

	@Autowired
	private RecommendService service;

	@Autowired
	private CafeService caService;

	@ApiOperation(value = "주제별 추천 리스트 보여주기")
	@GetMapping("/survey/list/theme/{theme}/{page}")
	public List<CafeDto> recommendAllByTheme(@PathVariable String theme,@PathVariable Integer page) {
		return service.recommendAllByTheme(theme,page);
	}
	
	@ApiOperation(value = "서베이 결과 추천 카페 3개 보여주기")
	@GetMapping("/survey/{type}")
	public List<CafeDto> recommendByType(@PathVariable String type) {
		return service.recommendByType(type);
	}
	
	@ApiOperation(value = "서베이 타입별 추천 카페 리스트 보여주기")
	@GetMapping("/survey/list/{type}/{page}")
	public List<CafeDto> recommendAllByType(@PathVariable String type,@PathVariable Integer page) {
		return service.recommendAllByType(type,page);
	}
	
	@ApiOperation(value = "로그인 유저의 서베이 결과 저장")
	@PutMapping("/survey/{type}/{uid}")
	public String setUserType(@PathVariable String type, @PathVariable String uid) {
		System.out.println("set user survey type");
		UserDto user=new UserDto();
		user.setId(uid);
		user.setSurvey(type);
		int cnt = service.setUserType(user);
		if (cnt > 0) {
			return "Success";
		}
		return "Failure";
	}
	
	@ApiOperation(value = "좋아요 기반 추천 리스트(많은 순)")
	@GetMapping("/like/count/{uid}")
	public List<CafeDto> recommendByLikeCount(@PathVariable String uid) {
		List<Integer> myCafeList = service.selectCafeLiked(uid);// 내가 좋아요 누른 카페들
		List<String> userList = new ArrayList<>();// 내가 좋아요 누른 카페들을 좋아요 누른 유저들
		List<Integer> othersCafeList = new ArrayList<>();// 다른 유저들이 좋아요 누른 카페들
		List<CafeDto> recommendList = new ArrayList<>();// 추천할 카페들

		for (Integer cafeno : myCafeList) {// userList 구하기
			List<String> tmpList = service.selectUserLiked(cafeno);
			for (String now : tmpList) {
				if (!now.equals(uid) && !userList.contains(now)) {
					userList.add(now);
				}
			}
		}
		for (String user : userList) {// othersCafeList 구하기
			List<Integer> tmpList = service.selectCafeLiked(user);
			for (Integer cafeno : tmpList) {
				if (!myCafeList.contains(cafeno) && !othersCafeList.contains(cafeno)) {
					othersCafeList.add(cafeno);
					recommendList.add(caService.select(cafeno));
				}
			}
		}
		Collections.sort(recommendList, new Comparator<CafeDto>() {

			@Override
			public int compare(CafeDto o1, CafeDto o2) {
				return -Integer.compare(o1.getLike_count(), o2.getLike_count());
			}
		});

		if (recommendList.size() > 10) {
			return recommendList.subList(0, 10);
		} else {
			return recommendList;
		}
	}

	@ApiOperation(value = "좋아요 기반 추천 리스트(많은 순)-비로그인")
	@GetMapping("/like/count")
	public List<CafeDto> recommendByLikeCount() {
		return caService.selectAllByLikeCount();
	}

	@ApiOperation(value = "스탬프 기반 추천 리스트(많은 순)")
	@GetMapping("/stamp/count/{uid}")
	public List<CafeDto> recommendByStampCount(@PathVariable String uid) {
		List<Integer> myCafeList = service.selectCafeStamped(uid);// 내가 좋아요 누른 카페들
		List<String> userList = new ArrayList<>();// 내가 좋아요 누른 카페들을 좋아요 누른 유저들
		List<Integer> othersCafeList = new ArrayList<>();// 다른 유저들이 좋아요 누른 카페들
		List<CafeDto> recommendList = new ArrayList<>();// 추천할 카페들

		for (Integer cafeno : myCafeList) {// userList 구하기
			List<String> tmpList = service.selectUserStamped(cafeno);
			for (String now : tmpList) {
				if (!now.equals(uid) && !userList.contains(now)) {
					userList.add(now);
				}
			}
		}
		for (String user : userList) {// othersCafeList 구하기
			List<Integer> tmpList = service.selectCafeStamped(user);
			for (Integer cafeno : tmpList) {
				if (!myCafeList.contains(cafeno) && !othersCafeList.contains(cafeno)) {
					othersCafeList.add(cafeno);
					recommendList.add(caService.select(cafeno));
				}
			}
		}
		Collections.sort(recommendList, new Comparator<CafeDto>() {

			@Override
			public int compare(CafeDto o1, CafeDto o2) {
				return -Integer.compare(o1.getStamp_count(), o2.getStamp_count());
			}
		});
		if (recommendList.size() > 10) {
			return recommendList.subList(0, 10);
		} else {
			return recommendList;
		}
	}

	@ApiOperation(value = "스탬프 기반 추천 리스트(많은 순)-비로그인")
	@GetMapping("/stamp/count")
	public List<CafeDto> recommendByStampCount() {
		return caService.selectAllByStampCount();
	}

	@ApiOperation(value = "좋아요 기반 추천 리스트(최근 순)")
	@GetMapping("/like/recent/{uid}")
	public List<CafeDto> recommendByLikeRecent(@PathVariable String uid) {
		List<Integer> myCafeList = service.selectCafeLiked(uid);// 내가 좋아요 누른 카페들
		List<String> userList = new ArrayList<>();// 내가 좋아요 누른 카페들을 좋아요 누른 유저들
		List<Integer> othersCafeList = new ArrayList<>();// 다른 유저들이 좋아요 누른 카페들
		List<CafeDto> recommendList = new ArrayList<>();// 추천할 카페들

		for (Integer cafeno : myCafeList) {// userList 구하기
			List<String> tmpList = service.selectUserLiked(cafeno);
			for (String now : tmpList) {
				if (!now.equals(uid) && !userList.contains(now)) {
					userList.add(now);
				}
			}
		}
		for (String user : userList) {// othersCafeList 구하기
			List<Integer> tmpList = service.selectCafeLiked(user);
			for (Integer cafeno : tmpList) {
				if (!myCafeList.contains(cafeno) && !othersCafeList.contains(cafeno)) {
					othersCafeList.add(cafeno);
					recommendList.add(caService.select(cafeno));
				}
			}
		}
		Collections.sort(recommendList, new Comparator<CafeDto>() {

			@Override
			public int compare(CafeDto o1, CafeDto o2) {
				return -Integer.compare(o1.getRecent_like(), o2.getRecent_like());
			}
		});

		if (recommendList.size() > 10) {
			return recommendList.subList(0, 10);
		} else {
			return recommendList;
		}
	}

	@ApiOperation(value = "좋아요 기반 추천 리스트(최근 순)-비로그인")
	@GetMapping("/like/recent")
	public List<CafeDto> recommendByLikeRecent() {
		return caService.selectAllByLikeRecent();
	}

	@ApiOperation(value = "스탬프 기반 추천 리스트(최근 순)")
	@GetMapping("/stamp/recent/{uid}")
	public List<CafeDto> recommendByStampRecent(@PathVariable String uid) {
		List<Integer> myCafeList = service.selectCafeStamped(uid);// 내가 좋아요 누른 카페들
		List<String> userList = new ArrayList<>();// 내가 좋아요 누른 카페들을 좋아요 누른 유저들
		List<Integer> othersCafeList = new ArrayList<>();// 다른 유저들이 좋아요 누른 카페들
		List<CafeDto> recommendList = new ArrayList<>();// 추천할 카페들

		for (Integer cafeno : myCafeList) {// userList 구하기
			List<String> tmpList = service.selectUserStamped(cafeno);
			for (String now : tmpList) {
				if (!now.equals(uid) && !userList.contains(now)) {
					userList.add(now);
				}
			}
		}
		for (String user : userList) {// othersCafeList 구하기
			List<Integer> tmpList = service.selectCafeStamped(user);
			for (Integer cafeno : tmpList) {
				if (!myCafeList.contains(cafeno) && !othersCafeList.contains(cafeno)) {
					othersCafeList.add(cafeno);
					recommendList.add(caService.select(cafeno));
				}
			}
		}
		Collections.sort(recommendList, new Comparator<CafeDto>() {

			@Override
			public int compare(CafeDto o1, CafeDto o2) {
				return -Integer.compare(o1.getRecent_stamp(), o2.getRecent_stamp());
			}
		});
		if (recommendList.size() > 10) {
			return recommendList.subList(0, 10);
		} else {
			return recommendList;
		}
	}

	@ApiOperation(value = "스탬프 기반 추천 리스트(최근 순)-비로그인")
	@GetMapping("/stamp/recent")
	public List<CafeDto> recommendByStampRecent() {
		return caService.selectAllByStampRecent();
	}

	@ApiOperation(value = "스탬프 기반 추천 리스트(많은 것중에 최근 순)")
	@GetMapping("/stamp/count/recent")
	public List<CafeDto> recommendByStampCountRecent() {
		List<CafeDto> list = caService.selectAllByStampCount();

		Collections.sort(list, new Comparator<CafeDto>() {

			@Override
			public int compare(CafeDto o1, CafeDto o2) {
				return -Integer.compare(o1.getRecent_stamp(), o2.getRecent_stamp());
			}
		});

		return list;

	}
}
