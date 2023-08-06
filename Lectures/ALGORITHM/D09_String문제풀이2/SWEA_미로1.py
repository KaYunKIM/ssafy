def find(sr,sc):
    dr = [-1,0,1,0]     #사방탐색을 위한 델타
    dc = [0,1,0,-1]
    s = []
    visited = [[0 for _ in range(N)] for _ in range(N)]     #방문배열
    s.append([sr,sc])
    visited[sr][sc] =1          #시작점을 방문했다고 표시
    while s:                    #스택에 자료가 있는 동안
        cur = s.pop()           #스택에서 하나 꺼내옴 -> 현재위치
        for k in range(4):
            nr = cur[0] + dr[k]     #새로운 좌표 계산
            nc = cur[1] + dc[k]
            if maze[nr][nc] == 3:   #도착점을 찾으면
                return True
            elif maze[nr][nc] == 0 and visited[nr][nc] == 0:    #새로운 좌표가 길이고 아직 방문 안했을 때
                s.append([nr,nc])   #스택에 새로운 좌표 넣기
                visited[nr][nc] = 1

T = 10
N = 16
for tc in range(1,T+1):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:       #출발점이면 시작
                if find(i,j):         #탐색하고 결과가 True면
                    result = 1        #result를 1로
    print('#{} {}'.format(tc, result))