export default{
    URL: 'https://i3a203.p.ssafy.io:5000/api',
    ROUTES: {
        //accounts 
        signup: '/user/signup',
        login: '/user/login',
        mypage: '/user',

        //post
        postList: '/post/list/',
        userPostList: '/post/list/user/1/',
        cafePostList: '/post/list/cafe/1/',
        postDetail: '/post',
        postDelete: '/post/delete/',
        uploadImage: '/post/upload',

        //comment
        createComment: '/comment',
        commentList: '/comment/list/',
        deleteComment: '/comment/delete/',

        //like, stamp
        like: '/like',
        stamp: '/stamp',

        //follow
        follow: '/follow',
        
        //cafe
        cafeDetail: '/cafe/',
        cafeList: '/cafe/list/',
        cafeKeyword: '/keyword/keywords/',
        cafeMenu: '/menu/list/',

        //search
        cafeSearch: '/cafe/search/',
        keywordSearch: '/keyword/cafelist/',
        userSearch: '/user/search/',

        //geo
        geolocation: '/cafe/geolocation/',

        //survey
        surveyResult: '/recommend/survey/',

        //recommend
        recommend: '/recommend/',
    }
}