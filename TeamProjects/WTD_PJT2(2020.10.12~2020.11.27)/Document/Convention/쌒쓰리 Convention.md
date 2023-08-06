## 쌒쓰리 Convention

#### 1. Git :zap:

1. 브랜치 분리

   - **master** - **develop, docs**-  **frontend/backend** - **[type]/[기능명]** 
   - **push 전에 pull부터 받을 것!!!**
   - 팀원들은 frontend와 backend에서 따로 feature 생성해서 push 후 PR 요청
   - document는 docs에 push 
   - feature > frontend/backend , frontend/backend > develop, develop > master 머지는 가윤 팀원이 담당

   

2. 영어만 사용하며, 첫 글자를 대문자로 하여 총 70자 이내

   - JIRA 이슈 번호 마지막에 추가할 것 ::star:**이슈번호는 스토리 단위**

   - 마침표 사용 X

   - 명령어 형식으로 작성

   - Type 종류

     - feat: 기능 추가 (Create, Update 사용)

     - fix: 버그 수정
     - refactor: 코드 리팩토링 (코드 중복 제거, 기능 변화없이 코드 스타일 변화 등)
     - docs: 문서

     

3. 커밋 메시지 예시

   ```
   feat/login: Create Login.vue, S03P22A305-2
   ```

   ```
   fix/login: Fix Login.vue, S03P22A305-2
   ```

   ```
   refactor/login: Refactor Login.vue, S03P22A305-2
   ```

   ```
   docs/presentation: Upload Presentation
   ```

   