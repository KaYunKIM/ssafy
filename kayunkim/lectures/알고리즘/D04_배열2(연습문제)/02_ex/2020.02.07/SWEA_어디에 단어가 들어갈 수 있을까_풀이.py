import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0   #단어를 넣을 수 있는 곳 개수
    for i in range(N):
        words = 0  #빈칸 수
        current = 0  #현재 위치
        while current < N:
            if matrix[i][current] == 1:     #검사 위치가 1일 때
                words += 1
                if words == K and current == N-1:
                    cnt+=1
            else:                       #검사 위치가 0일 때
                if words == K:
                    cnt+=1
                words = 0
            current+=1

    for i in range(N):
        words = 0  #빈칸 수
        current = 0  #현재 위치
        while current < N:
            if matrix[current][i] == 1:     #검사 위치가 1일 때
                words += 1
                if words == K and current == N-1:
                    cnt+=1
            else:                       #검사 위치가 0일 때
                if words == K:
                    cnt+=1
                words = 0
            current += 1
    print('# {} {}'.format(tc,cnt))
