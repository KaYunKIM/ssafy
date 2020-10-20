package com.cafe.service.jwt;

import com.cafe.dto.TokenSet;
import com.cafe.dto.UserDto;

public interface JwtService {
	TokenSet createTokenSet(UserDto user);
	TokenSet refreshAccessToken(String refreshToken);
	TokenSet refreshTokenSet(String refreshToken);
	//Map<String,Object> get(String key);
	UserDto getUser(String jwt, String secretKey);
	//int getUserId();
	boolean isValidToken(String jwt, String secretKey);
}
