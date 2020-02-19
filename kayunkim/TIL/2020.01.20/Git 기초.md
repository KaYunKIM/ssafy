# Git 기초

> Git은 분산형버전관리시스템(DVCS)이다.
>
> 소스코드의 이력을 관리하고, 협업 단계에서 활용 가능하다.



> ## 0. 기본 설정
>
> 윈도우에서  git을 활용하기 위해서는 `git bash`가 필요하다.

​     설치 이후에 `commit`을 작성하는 `author`설정이 필요하다.

> ```
> $ git config --global user.name "github username"
> $ git config --global user.email "github email"
> ```

설정 내용을 확인하기 위해서는 아래의 명령어를 입력한다.

```
$ git config --global -1
```



## gitignore 

프로젝트를 진행할 때, `git`으로 관리하지 않을 파일 혹은 폴더들을 설정할 수 있다.

```
*.xlsx                  #확장자가 xlsx인 모든 파일
a.txt					# a.txt파일
.ipynb_checkpoints/		# .ipynb_checkpoints 폴더
```

프로젝트 시작 시 어떤 내용을 담아야할지 모르겠다면, gitignore에서 검색한다.

예) `python`, `jupyter notebook`



## 로컬 저장소에서 활용하기

### 1. git 저장소 설정

특정 프로젝트 폴더에서  `git`을 활용하기 위해서는 아래의 명령어를 입력한다.

```
$git init
```

- 해당 디렉토리 내 `git`이라는 숨김 폴더가 생성되며, 모든 `git`과 관련된 동작은 해당 폴더에 기록된다.

- git bash에서 (master)라는 브랜치 정보가 표기된다.

  

  ### 2. add

  `git`에서 commit할 대상 파일을 `staging area` 로 이동시키는 명령어이다.

  ```
  $git add a.txt 			#특정 파일을 stage
  $git add images/		#특정 폴더를 stage
  $git add . (#모든 파일 한번에 추가) # 모든 디렉토리 파일 및 폴더를 stage
  ```



**항상 `git status` 명령어를 통해서 현재 상태를 확인하는 것이 중요하다!!!**



### 3. commit

git에서 이력을 남기기 위해서는 `commit`을 통해서 진행한다.

`commit`을 남길 때에는 항상 commit 메세지를 작성한다.

메세지는 해당 이력에 대한 정보를 담는다.

```
$ git commit -m "커밋메시지"
```

커밋 이력을 확인하기 위해서는 아래의 명령어를 활용한다.

```
$ git log
```

이후 변경 사항이 발생하면, `add` -> `commit` 을 한다.

`add`: 커밋할 대상 파일 선정

`commit`: 이력의 확정



# 원격 저장소(remote repository) 활용하기

> 원격 저장소를 제공해주는 서비스는 다양하다.
>
> 우리는 github를 기준으로 활용.



### 0. 기본설정

github에 비어있는 저장소(repository) 생성



### 1. 원격 저장소 설정

```
$ git remote add origin https://~(원격저장소주소)
```

원격 저장소(remote)를 origin이라는 이름으로 https://~로 설정한다.

아래의 명령어를 통해 저장된 원격 저장소 목록 확인할 수 있다.

```
$ git remote -v
```

혹시 잘못 설정되었다면, 아래의 명령어 통해 삭제 가능하다.

```
$ git remote rm origin
$ git remote -v
```



### 2. push

원격 저장소에 업로드 하기 위해서는 `push` 명령어가 필요하다.

```
$ git push origin master
```

`origin`으로 설정된 원격 저장소에  `push`한다.

변경된 사항 (`commit`)이 발생했을 때, `git push origin master` 명령어를 통해서 매번 업로드 해줄 수 있다.