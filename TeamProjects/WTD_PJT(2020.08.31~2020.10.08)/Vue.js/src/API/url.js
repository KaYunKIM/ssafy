// URL에 CRUD사용 x
// 동사형x 명사형 사용

export default{
	URL: 'http://j3a511.p.ssafy.io:8000',
	//URL: 'http://localhost:8000',
	ROUTES: {
		//accounts
		login: '/accounts/login/',
		join:  '/accounts/join/',
		mypage: '/accounts/profile/',

		//projects
		projects: '/projects/',
		audio: '/projects/audio/',
		stt: '/projects/stt/',


		// schedules
		schedules: '/schedules/'
	}, 
}
