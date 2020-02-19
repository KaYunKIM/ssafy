di = [-1,0,1,0]
dj = [0,1,0,-1]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(M):
            k = arr[i][j]
            sum = k
            print(sum, end = ' ')
            for d in range(4):      #탐색방향 정하기
                newi, newj = i+di[d], j+dj[d]
                h = 1               #탐색깊이
                while 0 <= newi < N and 0 <= newj < M and h<=k:
                    sum += arr[newi][newj]  #새로운 좌표의 값 누적하기
                    h+= 1
                    newi = newi + di[d]      #지정된 방향으로 좌표 갱신
                    newj = newj + dj[d]
            if maxV < sum:
                maxV = sum
     print('#{} {}'.format(tc,max))
