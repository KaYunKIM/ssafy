## Django_project4 일기

전체적인 큰 흐름으로는 회원가입,로그인,로그아웃을 수행하는 `accounts` 앱과,

게시글 작성, 수정, 삭제와 댓글 작성,삭제 등을 관리하는 `community` 앱을 구현해 보았습니다.




>`accounts`와 `community`앱 별로 구현 과정을 설명하고 있습니다.

## accounts

- `UserCreationForm` 과 `AuthenticationForm` 이외에 `follower` 와 `following`  기능을 추가하기 위하여 `models.py` 에서는 `User ` 모델을, `forms.py`에서는  `CustomUserCreationForm`  를 새롭게 생성해서 사용했습니다.

- Url path를 `signup/`, `login/`, `logout/` 패턴으로 설정하고, follow 기능을 위한 profile detail 페이지와 follow 기능   수행을 위한 url을 추가로 생성했습니다. `views.py`에서 `signup`메소드와 `login`메소드는 `GET`요청과 `POST`요청으로 분기했습니다.

- **views.py** 

  - signup

    -  `CustomUserCreationForm`을 활용하여 모델에 아이디, 비밀번호, 비밀번호 확인 칸을 폼에 담아 보여줍니다.
    - 유효성 검사를 통해 유효하다면 게시글 전체 목록 페이지로 redirect하고 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - Login

    - `POST`요청을 받았을 때는, `AuthenticationForm`으로 유효성 검사를 합니다.
    - 유효성 검사를 통해 유효하다면 `request.GET.get('next')`로 받아온 로그인 이전의 URL로 redirect하고 처음부터 로그인 페이지로 접근했다면, 영화 목록 페이지로 redirect합니다.
    - 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - logout

    - 로그인을 했을 때 로그아웃을 할 수 있게 `@login_required` 를 import해서 사용했습니다.

  - detail

    - `User` 모델을 받아서 user profile 관련 정보(작성 review 등)를 context에 담아서 조회가 가능하게 했습니다.

  - Follow

    - `User` 모델을 받아서 해당 profile user가 아닌 사람이 접근 했을 때, follow를 했으면 follow 취소하고, 안 했으면 follow를 할 수 있습니다.

    

## community

- `Movie`,  `Review`와  `Comment`클래스를 models.py에서 만들었습니다. 

- 사용자와 리뷰를, 영화와 리뷰를 `1:N`으로 관계지어주기 위해 Review모델의 movie필드를 만들고 `ForeignKey`로 연결했습니다.

- 다수의 리뷰에 다수의 like를 받기 위한 `M:N`으로 관계지어주기 위해 `ManyToManyField`를 활용했습니다.

- Movie 데이터는 따로 받지 않고 게시판 관리 상 관리자만 추가할 수 있게 하기 때문에 Movie를 제외한 forms.py에서 `ReviewForm`과  `CommentForm`에 원하는 필드만 담아서 `ModelForm`을 만들어주고 migrate를 실행해 데이터베이스에 반영해주었습니다.

- admin.py에서 models.py의 `Movie`를 import해서 admin사이트에 등록하고 `createsuperuser`를 했습니다.

- Image를 삽입하기 위해 setting.py에서 `MEDIA_ROOT`와 `MEDIA_URL`을 만들고 url에서 경로 설정을 해주었습니다.

- **views.py**

  - index

    - Movie의 모든 필드를 가져와 context에 담아 전체 영화 목록 페이지에서 보여주었습니다. 각 영화는 bootstrap의 card 기능을 사용해 정보를 보여주고, detail페이지로 이동할 수 있게 했습니다.
  - movie_detail
    - 선택한 영화의 필드들을 context에 담아서 영화 리뷰와 작성자를 보여줄 수 있게 했습니다.
  - review_detail

    - `get_object_or_404`를 import 해서 영화 pk값과 리뷰 pk값을 각각 넘겨받은 pk값으로 설정하고, 존재하지 않는다면 에러메세지를 뜨게 했습니다.
    - 해당 HTML페이지에서 기본으로 `review_title` , `movie_title` , `rank` , `content` 를 보여주고, 좋아요 기능도 추가하고, 해당 게시글에 달린 댓글의 작성자와 댓글 내용을 보여주었습니다.

  - review_create

    - `@login_required`로 사용자의 로그인 여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.
    - 유효성 검사를 통해 유효하다면 `ReviewForm`에서 받아온 review에 해당 유저를 추가해주고, 저장한 후 영화 상세 페이지로 redirect해줍니다.
    - 만약 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - review_edit

    - `@login_required`를 import해 로그인 전이라면, 로그인 페이지로 안내했습니다.
    - html에서 분기를 사용해 게시글 작성자인지를 확인하고, 맞다면 기존 리뷰 데이터를 리뷰폼에 담아 제공하고 유효성 검사를 통해 저장 후 리뷰 상세페이지로 redirect합니다.
    - 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - review_delete

    -  `@login_required`로 사용자의 로그인 여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.

    - html에서 분기를 사용해 게시글 작성자인지를 확인하고, 맞다면 삭제 버튼을 보이게 해서 삭제할 수 있게 했습니다.  

  - comment_create

    - `if request.user.is_authenticated:` 로 사용자의 로그인여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.
    - `CommentForm`으로 유효성 검사를 한 다음 유효하다면 `CommentForm`에 담긴 정보를 가져온 다음 현재 사용자 정보와 리뷰를 데이터베이스에 저장해주고, 리뷰 페이지로 영화pk값과 리뷰 pk값을 같이 넘겨주었습니다. 

  - Comment_edit

    - comment_edit기능을 구현하려고 했지만, 따로 별도의 html 페이지를 만들지 않고 리뷰 페이지에서 직접 리뷰 작성을 할 수 있게 만들었기 때문에 댓글 수정 기능은 활용할 수 없었습니다.

  - comment_delete

    - `@login_required`를 import해 로그인 전이라면, 로그인 페이지로 안내했습니다.
    - 해당 글의 댓글 작성자가 현재 요청한 사용자와 일치한다면 댓글을 삭제하고 리뷰 상세페이지로 redirect합니다.

  - like

    - 해당 리뷰 정보를 가져와서 만약 `like`를 했다면 `unlike`로 처리하고, 그게 아니라면, `like`를 하고 `like`한 유저에 추가한 후 숫자를 count할 수 있게 구현했습니다.

      

## templates

- `base.html`을 만들어 별도의`nav.html` 을 포함시켜주었고, 와` block content`를 만들고 모든 HTML파일에서 `extends`로 활용했습니다.




## 느낀점

- 오늘 프로젝트의 self-assesment 점수는 10점 만점의 8점입니다.
- 두 번째 페어 프로그래밍인 만큼, 더 좋은 팀워크를 발휘했다고 생각합니다.
- 지속적으로 대화하며 의견을 공유하고, 막히는 부분이 생기면 즉시 대화를 통해 해결방안을 찾아 빠른 문제해결이 가능했습니다.
- 오늘 저의 역할은 driver 5: navigator 5이었고, 그만큼 실제 코딩과 의견제안을 골고루 수행하며 적극적으로 참여했기 때문입니다.



## 아쉬운 점

- 시간 부족에 대한 아쉬움이 있었습니다.

- 더 세부적인 스타일링이라던지, 영화 검색api를 활용하여 완성하지 못한점이 아쉽습니다.

  

## 좋았던 점

- 이번 프로젝트를 통해서 지금까지 배웠던 `django`의 내용들을 쭉 훑어보며 복습할 수 있었고, 확실치 않았던 개념들 혹은 알고보니 잘 모르고 있던 부분들을 다시 한번 짚고 넘어갈 수 있어서 좋았습니다.
- 지난번 프로젝트 때 아쉬웠던 부분인 처음부터 명세를 보고 전체적인 로드맵을 그려보지 못했던 것을 이번에는 할 수 있어서 프로젝트의 진행이 원활하게 됐고, 제가 개인적으로 많은 부분을 이해하며 구현할 수 있어서 좋았습니다.
