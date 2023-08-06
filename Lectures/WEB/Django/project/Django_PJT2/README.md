<h1>오늘의 Django일기</h1>


1. 먼저 ``Django_pjt2``  프로젝트와 ``community``  앱을 생성하고 settings에가서 ``ALLOWED_HOST`` 와 ``INSTALLED_APPS  `` 추가,  ``BASE_DIR``  등을 설정해준다.
2. ``models.py`` 에서 원하는 필드명과 자료형을 설정해준다.
3. ``forms.py`` 를 생성하고  ``ModelForm`` 을 사용한다. Meta 클래스를 사용해서``models.py`` 에서 만든 클래스의 모든 필드를 가져온다.

4. ``admin.py`` 에서 ``models.py`` 의 Review 클래스를 가져와 어드민 사이트에 등록할  ``ReviewAdmin`` 클래스를 만들어 함께 등록한다.
5. ``community/urls.py`` 를 새로 생성하고, ``app_name``을 지정해 url:값의 형태로 사용할 path를 name과 함께 만들어준다.

6. - 공유 Template

     Templates/base.html을 생성하고 ``nav_bar`` 와 다른 html들에서 공유할  ``block content`` 를 만들어 준다

   - 새로운 리뷰 생성

     ``views.py`` 에서 ``create` 함수를 만들어 요청이 POST이고 유효한 data일 경우, 작성한 data를 저장하고 해당 detail페이지로 redirect한다. 요청이 GET일 경우, 혹은 유효하지 않은 data일 경우, form에 담긴 내용의 context를 생성 페이지로 반환한다.

   - 전체 리뷰 목록 조회

     ``review_list.html`` 페이지에서 for문을 활용해 전체 저장되어 있는 data를 가져와서 조회한다. 상단에는 ``NEW`` 버튼으로 생성페이지로 가는 링크를 걸고, 제목에도 링크를 걸어 해당 상세 페이지로 이동하게 한다. 이때 detail링크와 함께 아이디값을 넘겨준다.

   - 단일 리뷰 상세조회

     ``views.py`` 에서 ``detail`` 함수를 만들어 Review data를 가져오고 data가 없다면 get_object_or_404로 오류페이지를 context에 담아 상세페이지로 반환한다.

     `review_detail.html` 페이지에서는 상세 필드를 하나씩 변수로 값을 받아오고 `EDIT` `DELETE` `BACK` 버튼과 링크를 생성해 버튼에는 해당 링크와 pk값을 같이 넘겨주고, 링크는 전체 목록 페이지로 넘겨준다.

   - 기존 리뷰 수정

     ``views.py`` 에서 ``update`` 함수를 만들어 요청이 POST일 경우, 기존 data를 instance로 받아 수정하고,  저장 후 해당 detail페이지로 redirect한다. 요청이 GET일 경우 혹은 POST요청으로 받은 data가 유효하지 않을 경우, 각각 받아온 기존의 데이터를 다시 수정 페이지로 반환한다.

   - 기존 리뷰 삭제

     ``views.py`` 에서 ``delete `` 함수를 만들어 요청이 POST일 경우에만 받아서 유효한 데이터이면 삭제하고, 아니면 에러메세지를 띄운다.