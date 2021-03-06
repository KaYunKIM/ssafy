# Django_pjt3 일기

전체적인 큰 흐름으로는 회원가입,로그인,로그아웃,회원탈퇴 등 회원을 관리하는 `accounts` 앱과,

게시글 작성, 수정,삭제와 댓글 작성,삭제 등을 관리하는 `community` 앱을 구현해 보았습니다.





>아래는 명세 순서대로 `accounts`와 `community`앱 별로 구현 과정을 설명하고 있습니다.
## accounts

- `UserCreationForm` 과 `AuthenticationForm` 을 사용할 수 있기 때문에 따로 model과 form설정이 필요 없다.

- Url path를 `/signup/`, `/login/`, `/logout/` 패턴으로 설정하고, 명세에 나와있는 데로 `views.py`에서 `signup`메소드와 `login`메소드는 `GET`요청과 `POST`요청으로 분기하고, `logout`메소드는 `POST`를 선택하여 진행했습니다.

- **views.py**

  - signup

    - `UserCreationForm`을 활용하여 아이디, 비밀번호, 비밀번호 확인 칸을 폼에 담아 보여줍니다.
    - 유효성 검사를 통해 유효하다면 게시글 전체 목록 페이지로 redirect하고 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - Login

    - `if request.user.is_authenticated:`으로 로그인이 되어있다면, 게시글 전체 목록 페이지로 redirect하고 아직 로그인 전이라면 `AuthenticationForm`으로 유효성 검사를 합니다.
    - 유효성 검사를 통해 유효하다면 `request.GET.get('next')`로 받아온 로그인 이전의 URL로 redirect하고 처음부터 로그인 페이지로 접근했다면, 게시글 전체 목록 페이지로 redirect합니다.
    - 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - logout

    - POST요청 방식으로 선택해 `@require_POST`를 사용하고, 로그인을 했을 때 로그아웃을 할 수 있게 `@login_required`도 import해서 사용했습니다.

  - delete_user

    - logout과 마찬가지로 `@require_POST` 와 `@login_required` 를 import하고 해당 유저의 pk값을 받아와서 User정보 중 pk값을 가져와 같은 유저라면, 회원 삭제를 진행하고, 바로 회원가입 페이지로 넘겨주어 질척임의 끝판왕을 보여주었습니다.



## community

- 명세에서 요구하는 필드들로 구성된 `Review`와  `Comment`클래스를 models.py에서 만들어주고, forms.py에서 `ReviewForm`과  `CommentForm`에 원하는 필드만 담아서 `ModelForm`을 만들어주고 migrate를 실행해 데이터베이스에 반영해주었습니다.

- admin.py에서 models.py의 `Review`와 `Comment`를 import해서 admin사이트에 등록하고 `createsuperuser`를 했습니다.

- Url patterns는 `index`, `review_create`, `detail`, `review_update`, `review_delete`, `comment_create, comment_delete`로 name을 설정해 경로를 지정해주었습니다.  이중 views.py에서 `review_delete`와 `comment_delete`메소드에서 POST요청 방식을 선택했습니다.

- **views.py**

  - review_create

    - `if request.user.is_authenticated:` 로 사용자의 로그인여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.
    - 유효성 검사를 통해 유효하다면 `ReviewForm`에서 받아온 review에 해당 유저를 추가해주고, 저장한 후 게시글 상세 페이지로 redirect해줍니다.
    - 만약 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - index

    - Review의 모든 필드를 가져와 reviews instance를 만들어주고 이를 context에 담아 게시글 전체목록 페이지에서 보여주었습니다. HTML페이지에 `review.title`에 링크를 걸어 해당 게시글 상세페이지로 이동할 수 있게 설정했습니다.

  - review_detail

    - `get_object_or_404`를 import 해서 게시글의 pk값과 넘겨받은 pk값이 일치하지 않을 때 404에러 페이지를 보여주었습니다.
    - 해당 HTML페이지에서 기본으로 `title` , `movie_title` , `rank` , `content` , `created_at` , `updated_at`을 보여주고, 해당 게시글에 달린 댓글의 작성자와 댓글 내용을 보여주었습니다.
    - `if comment.user == request.user`로 댓글 작성자에게만 해당 댓글 오른쪽에 댓글삭제 링크를 보여주었습니다.
    - `if request.user.is_authenticated`로 만약 로그인을 한 사람이라면, 해당 게시글에 대한 댓글 작성이 가능하고,  하단에 `if comment.user == request.user`로 만약 게시글 작성자라면 수정, 삭제 버튼이 나타나게 구현했습니다.

  - review_update

    - `if request.user.is_authenticated:` 로 사용자의 로그인여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.
    - `if review.user == request.user:`로 게시글 작성자인지를 확인하고, 맞다면 기존 리뷰 데이터를 리뷰폼에 담아 제공하고 유효성 검사를 통해 저장 후 상세페이지로 redirect합니다. 게시글 작성자가 아니라면 바로 상세페이지로 redirect합니다.
    - 유효하지 않거나 GET요청방식으로 받았을 때는 사용자가 입력했던 데이터를 폼에 담아 다시 보여줍니다.

  - review_delete

    - `@require_POST`와 `@login_required`를 활용해 POST요청방식을 선택하고 로그인 페이지로 안내했습니다.

    - `if request.user.is_authenticated:` 로 사용자의 로그인여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.
    - `if review.user == request.user:`로 게시글 작성자인지를 확인하고, 맞다면 Review와 pk값을 받아온 것 유저와 현재 사용자가 일치하면, 게시글을 삭제하고, 만약 게시글 작성자가 아니라면 바로 상세페이지로 redirect합니다.

  - comment_create

    - `@login_required`를 import해 로그인 전이라면, 로그인 페이지로 안내했습니다.

    - `if request.user.is_authenticated:` 로 사용자의 로그인여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.
    - `CommentForm`으로 유효성 검사를 한 다음 유효하다면 `CommentForm`에 담긴 정보를 가져온 다음 유저 현재 사용자로 추가해주고, 게시글을 pk값과 같이 받아온 게시글로 저장해줬습니다.
    - 만약 데이터가 유효하지 않다면, 게시글 상세 페이지로 redirect해주었습니다.

  - comment_delete

    - `@login_required`를 import해 로그인 전이라면, 로그인 페이지로 안내했습니다.

    - `if request.user.is_authenticated:` 로 사용자의 로그인여부를 확인하고, 로그인이 안 된 상태라면, 로그인 페이지로 안내합니다.

    - 댓글 pk값을 넘겨받은 것의 작성자와 현재 사용자가 같다면 댓글을 삭제하고 게시글 상세페이지로 redirect합니다.



## templates

- `base.html`을 만들어 `navbar`와` block content`를 만들고 `bootstrap`을 설정해주어 모든 HTML파일에서 `extends`로 활용했습니다.

- 먼저 전체 리뷰 목록페이지를 보여주고, `user.is_authenticated` if문을 활용하여 로그인 했을 때는 유저네임과 로그아웃 버튼을 보여주고, 로그아웃 했을 때는 로그인과 회원가입 링크를 보여주었습니다.


