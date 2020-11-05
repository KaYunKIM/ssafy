// URL에 CRUD 사용x
// 동사형x 명사형 사용

export default{
	URL: 'http://k3a305.p.ssafy.io:8080',
	// URL: 'http://localhost:8000',
	ROUTES: {
		//accounts
		login: '/accounts/login/',
		join:  '/accounts/join/',
		user: '/accounts/user/',
		mypage: '/accounts/profile/',

		//projects
		projects: '/projects/',
		audio: '/projects/audio/',
		stt: '/projects/stt/',

		// schedules
		schedules: '/schedules/'
	}, 
}
