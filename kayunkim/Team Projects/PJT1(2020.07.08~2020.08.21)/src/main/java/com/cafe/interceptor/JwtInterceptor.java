package com.cafe.interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.cafe.annotation.LoginRequired;
import com.cafe.dto.TokenSet;
import com.cafe.service.error.AuthenticationException;
import com.cafe.service.jwt.JwtService;
import com.cafe.service.jwt.JwtServiceImpl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

@Component
public class JwtInterceptor extends HandlerInterceptorAdapter {
	private static final String HEADER_ACCESS = "ACCESS_TOKEN";
	private static final String HEADER_REFRESH = "REFRESH_TOKEN";

	@Autowired
	private JwtService jwtService;

	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		
		if (handler instanceof HandlerMethod){
			HandlerMethod hm = (HandlerMethod) handler;
			
			jwtService = new JwtServiceImpl();
			String accessToken = request.getHeader(HEADER_ACCESS);
			final String refreshToken = request.getHeader(HEADER_REFRESH);

			// refreshToken이 있는 경우
			// accessToken이 만료되어서 새로 재발급 해주어야 함
			if(refreshToken != null){
				TokenSet tokenSet = jwtService.refreshAccessToken(refreshToken);
				accessToken = tokenSet.getAccessToken();	// 재발급된 accessToken
				//response.addHeader(HEADER_ACCESS, accessToken);	// 응답 header로 새로 보내주기
				//response.addHeader(HEADER_REFRESH, refreshToken);
				//response.setHeader(HEADER_ACCESS, accessToken);
				//response.setHeader(HEADER_REFRESH, refreshToken);
				System.out.println(accessToken);
				System.out.println("access token 재발급");
			}

			if (hm.hasMethodAnnotation(LoginRequired.class)){
				//System.out.println("login 필요");
				if(accessToken == null || !jwtService.isValidToken(accessToken, JwtServiceImpl.AT_SECRET_KEY)){
					throw new AuthenticationException("로그인되어있지 않습니다");
				}
			}
		}
		
		// if (request.getMethod().equals("OPTIONS")) {
		// 	return true;
		// }
		// if (token != null && jwtService.isValidToken(token, jwtService.getKey())) {
		// 	return true;
		// } else {
		// 	throw new UnauthorizedException();
		// }
		return super.preHandle(request, response, handler);
	}
}
