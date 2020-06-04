## Vue_pjt1

- 이번 Vue.js 프로젝트는 채원이와 함께 `pair-programming`으로 진행했고, App 프로젝트 내 MovieView와 VideoView로 각자 파트를 나누어 개발했습니다.
- 저는 VideoView 파트를 맡아 views 안에 `VideoView.vue`를 만들고 하위 components로 `VideoSearch.vue`, `VideoItem.vue`, `VideoItemDetail.vue`를 만들어 구현했습니다.
- 먼저 큰 흐름으로는, `VideoSearch.vue`에서 검색어를 받아 `VideoView.vue` 로 보내주고,  `VideoView.vue` 에서는 `VideoItem.vue` 으로 비디오들을 배열로 받아 넘겨 준 다음, 다시 `VideoItemDetail.vue` 로 개별 비디오들을 하나씩 넘겨주어 비디오 영상을 보여주었습니다.



## App.vue

- 기본적인 navbar를 구현하고, navbar의 MovieApp을 클릭했을 때, resetPage함수를 호출해서 버튼이 클릭되었다는 데이터를 view에 넘겨줬습니다.



### VideoView.vue

- 영화예고편 검색 글과 `VideoSearch.vue` 에서 받아올 <VideoSearch>, 그리고 `VideoItem.vue` 으로 비디오 배열을 넘겨줄 <VideoItem>태그를 만들어 주었습니다.
- 유튜브에서 동영상을 받아올 api key와 url을 변수로 선언하고, key값은 숨겨주기 위해 .env.local에 따로 저장했습니다.
- components에서 가져온 VideoSearch와  VideoItem을 다시 내보내기 위해 export를 해주었고,  `VideoSearch.vue` 에서 newSearch이벤트가 발생할 때 getVideos라는 함수를 실행했습니다.
- getVideos라는 함수에는 유튜브 키워드 검색어 + 'trailer'를 붙여 해당 영화 예고편을 담은 url 세부 주소 요소들을 object형태로 담아 config 변수로 만들었고, 이를 axios.get으로 기본 api url과 함께 담아서 빈 videos 배열에 api로 가져온 5개의 값들을 넣어주었습니다.



#### VideoSearch.vue

- 검색창과 검색 버튼으로 `searchVideo`함수를 실행해 동시에 검색어를 담을 수 있도록 구현했습니다.
- `searchVideo `함수에는 빈 keyword 스트링에 검색 단어를 넣고 이를 newsearch라는 이름으로 `VideoView.vue`  에서 받을 수 있게 emit했습니다.



#### VideoItem.vue

- `VideoItemDetail.vue` 에게 video를 넘겨주기 위해 `VideoItemDetail.vue` 을 import 받아 export에 넣어주었습니다.
- props로 `VideoView.vue` 에서 videos 배열을 받아 오고 이를 다시 `v-for`로 video한개 씩을 꺼내어 video라는 이름으로 `VideoItemDetail.vue` 에게 넘겨주었습니다.



#### VideoItemDetail.vue

-  `VideoItem.vue` 에서 넘겨준 video를 받기 위해 props로 video object를 받고, iframe 태그에서 동영상을 보여주기 위한 주소를 computed에서 VideoUrl함수를 만들고 이를 변수로 사용해주었습니다.
- 동영상 제목들 중 ''와 같은 문자들을 변환하기 위해 lodash 패키지를 활용해서 정상적인 글자로 보이게끔 구현했습니다.



#### 총평

- Vue.js를 배운지 얼마되지 않아 프로젝트를 하게 돼서 완성하는데까지 시간이 오래걸렸지만, 기능 하나하나들을 구현하면서 다시 복습할 수 있었고, 짝꿍에게 계속 물어보면서 많이 배울 수 있었습니다.
- 처음 시작부터 업무 분담을 명확히 하고 중간중간 같이 명세도 꼼꼼히 보면서 프로젝트 진행상황을 바로바로 체크해 나갈 수 있었습니다.



> 홈페이지 배포 URL

```
https://loving-mahavira-7fc5a6.netlify.app/
```

