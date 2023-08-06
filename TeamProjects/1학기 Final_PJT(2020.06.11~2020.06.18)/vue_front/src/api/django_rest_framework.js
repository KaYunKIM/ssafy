export default {
    // 나중에 django가 돌고있는 서버 url로 바뀜
    URL: 'http:///localhost:8000',
    ROUTES: {
        // rest-auth, accounts
        'signup': '/rest-auth/signup/', 
        'login': '/rest-auth/login/',
        'logout': '/rest-auth/logout/',
        'profile': '/accounts/user/',
        'likeList': '/accounts/user/likes/',
        'birthdayList': '/accounts/user/birthday/',
        // movies
        'new': '/movies/new/',
        'recommendations': '/movies/recommendations/',
        'popular': '/movies/popular/',
        'like': '/movies/like/',
        // articles
        'articles': '/articles/',
    }
}