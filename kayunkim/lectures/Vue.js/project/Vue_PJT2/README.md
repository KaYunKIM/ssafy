# Vue_PJT2

- 이번 프로젝트는 Vue와 Django를 함께 사용해서 웹 개발을 했습니다.
- 데이터베이스는 Django의 `movie_api-master`를 활용했으며 Vue만 새롭게 구현했습니다.
- Vue 파트에서 크게 accouts와 articles로 나누어서 pair-programming으로 개발했고, 저는 articles의 `ArticleCreateView.vue`와 `ArticleListView.vue`를 맡았습니다.



## Router

게시글 조회를 위한 `ArticleListView`와 게시글 생성을 위한 `ArticleCreateView`페이지로 이동하기 위해` index.js`에서 path로 경로 설정을 해주었습니다.



## App.vue

이번 프로젝트의 최상위 컴포넌트인 App.vue에서 `router-link`를 사용해 목록과 글쓰기 탭을 nav-bar를 활용해 구현했습니다.`v-if`를 사용해서 로그인 되어있을 때만 글쓰기 버튼이 보이게 해주었습니다.



## views

#### ArticleCreateView

- data함수 안에 `articleInfo` 변수를 생성하여 title과 content를  연결시켜 주었습니다.
- `createArticle`이라는 메서드를 사용하여 해당 url 페이지 경로를 정의해주고, 인증된 사용자만 글을 작성할 수 있도록 쿠키의 key값을 사용해 게시글 정보와 함께 넘겨주었습니다.
- `articleInfo`에 담겨진 정보를 보여주기 위해 `v-model`을 사용하여 양방향으로 변경가능한 title과 content를 보여주었습니다.

#### ArticleListView

- data함수 안에 `article_list`를 빈 배열로 생성해서 게시글들을 담기 위해 준비해두었습니다.
- `getArticleList`라는 메서드를 사용하여 해당 url페이지 경로를 정의해주고, 해당 url에서 요청이 왔을 때, `article_list`에 응답으로 온 데이터를 넣어주었습니다.
- 에러가 발생하면 콘솔창에 에러를 출력시켰습니다.
- template에서는` v-for`문으로 `article_list`안에 담긴 article 하나하나의 정보를 보여주었습니다.



## 총평

Vue와 Django를 함께 사용하여 개발하는 것이 생각보다 까다롭고, 발생가능한 변수와 오류들이 많아 꼼꼼히 작업을 해야한다는 것을 느꼈습니다. 최종 프로젝트에서 두가지를 다 활용하려고 생각중에 있었는데, 그 전에 한번 이렇게 경험해볼 수 있어서 좋았고 많이 배울 수 있었습니다.

