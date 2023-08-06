## develop => master 충돌 해결 방법

- merge branch 나가기 & merge할 branch 삭제

```
git checkout develop
git branch -D master_merge
```

- master_merge 새로 만들기

```
git checkout -b master_merge origin/master
```



- 원격 저장소 작업 가져오기& devlop브랜치 이동 후 merge하기

```
git fetch origin
```

```
git checkout develop
```

```
git merge {{master_merge}}
```

![ĸó1](ĸó1.PNG)



- 그러면 다음과 같은 변동사항들을 확인할 수 있다.

![ĸó5](ĸó5.JPG)

- 현재까지 상황 add/commit/push 하기

```
git add .
git commit -m "commit message"
git push origin develop
```



![ĸó4](ĸó4.PNG)

- develop => master 브랜치 이동

```
git checkout master
```

- master => master|MERGING 브랜치 이동

```
git merge develop
```

![ĸó3](ĸó3.PNG)

![ĸó6](ĸó6.JPG)

```
git add . 
git commit -m "commit message"
git push origin master
```



![ĸó2](ĸó2.PNG)



- master_merge => (15eb223..) 브랜치 이동

```
git merge --no-ff master_merge
```

> CONFLICT, removing 등 충돌 진행상황 확인



```
git status
```

> new file, deleted 등 추가/삭제 파일 확인



- (15eb223) => (8e1f618) => develop 브랜치 이동

```
git add .
git commit -m "commit messge"
git push origin master

git checkout develop
```



- commit에 반영이 안될 때,

```
> git add --all
```



