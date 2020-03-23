## FLEX

- `flex` 이전에는 배치를 위해서 `float`, `position`을 통해 지정을 해야 했다.



### flex의 주요 개념

- `container`, `item`

  ```html
  <style>
    .container{
      display: flex;
    }
  </style>
  
  <div class = "container">
  	<div class = "item"></div>
  </div>	
  ```

- `Main axis`, `cross axis`

- flex 정의 시,

  - `main axis` 을 기준으로 배치가 시작된다. (기본은 `row`)

    - 만약, `row-reverse`로 지정하게 된다면, 오른쪽 끝부터 배치가 시작됨.

  - 모든 `item`은 기본적으로 행으로 배치된다.

    - `flex-direction`: `row` 값으로 기본 설정 됨

  - 모든 `item`은 `cross axis`을 모두 채운다.

    - `align-items` : `stretch` 값으로 기본 설정 됨

  - 모든 `item`은 본인의 너비 혹은 컨텐츠 영역만큼 너비를 가지게 된다.

    - 경우에 따라서, 본인이 지정받은 너비보다 작을 수 있다.

      - `flex-wrap: nowrap` 이 기본 값이기 때문

      - 전체 아이템의 너비의 합이 컨테이너 너비보다 작을 때

![Screen Shot 2020-03-23 at 오전 10.03](/Users/kayun_kim/Desktop/Screen Shot 2020-03-23 at 오전 10.03.png)

## FLEX 속성

### 1. Flex-grow

> flex-grow` 는 남은 너비를 비율로 나눠 가진다.

- 기본값: 0

  

### 2. Justify-content

> main 축을 기준으로 정렬한다.

- 기본값: `flex-start`
- Flex-start: 위 정렬
- Flex-end: 밑으로 정렬
- center: 가운데 정렬
- space-around: 균등 좌우 정렬(내부 요소 여백은 외곽 여백의 2배)
- space-between: 컨텐츠 내에서만 균일 영역으로 나눈다
- Space-evenly: 균등 정렬(내부 요소 여백과 외곽 여백 모두 동일): 전체, 왼쪽 오른쪽도 마진영역 준다



### 3. align-items

> cross 축 기준으로 정렬한다.

- 기본값: `stretch`
- stretch
- flex-start
- flex-end
- baseline
- Center



### 4. order

> 아이템의 순서를 정의할 수 있다.

- 기본값: 0
- 음수값도 가질 수 있음
- 기본값이 전부 0이기 때문데, 하나만 값을 주면 맨 오른쪽 또는 왼쪽으로 이동함



### 5. align-self

> 각 아이템에 직접 align 지정할 수 있음.