'''
그래프

비선형 자료구조
그래프 G는 (V,E)의 쌍이다
    V : 정점의 집합
    E : 간선의 집합      #시작점, 끝점 u,v => (1,2) (2,3) (1,3)
    정점은 독립된 개체로 동그라미로 표현
    간선 두 정점을 이어주는 개체로 선이나 화살표가 있는 선으로 표현
                                #무방향그래프        #방향그래프
인접
    u,v라는 간선이 있다면 정점 u와 정점 v가 연결되어 있음(인접하다)

그래프의 표현

    인접행렬로 표현
        크기가 V*V인 행렬
        두 정점 i,j를 잇는 간선이 있다면, 인접행렬의 i,j는 1, 아니면 0

    무방향 그래프
        양방향으로 간선이 존재한다는 의미이므로 대칭행렬
    방향 그래프
        대칭 아님

'''


'''
스택을 활용한 dfs 구현
    방문배열, 스택 준비
    시작점을 스택에 넣고 방문표시
    스택이 빌 때까지 반복
        스택에서 정점을 꺼내옴
        출력
        꺼내온 정점에 인접하고 
        스택에 넣은 정점 방문 표시
'''
def dfs(n,V):                   #시작점, 정점갯수
    visited = [0] * (V + 1)     #방문표시용 배열
    stack = [0]*V               #스택
    top = -1

    top+= 1
    stack[top] = n
    visited[n] = 1              #시작점을 스택에 넣고 방문했다고 표시

    while top >= 0:
        n = stack[top]          #스택에서 하나 꺼내오기
        top -= 1
        print(n, end = ' ')
        for i in range(1,V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                top+=1
                stack[top] = i
                visited[i] = 1

V,E = map(int,input().split())
edge = list(map(int,input().split()))
matrix = [[0]*(V+1) for _ in range(V+1)]
#matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    matrix[n1][n2] = 1      #무방향그래프이므로 둘 다 1
    matrix[n2][n1] = 1
for row in matrix:
    print(row)