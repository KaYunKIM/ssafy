import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    sum = 0
    for i in range(N):
        current = 0
        cnt = 0
        while current < N:
            if matrix[i][current] == 1:
                cnt += 1
                if cnt == K and current == N-1:
                    sum+=1
            else:
                if cnt == K:
                    sum+=1
                cnt = 0
            current+=1

    for i in range(N):
        current = 0
        cnt = 0
        while current < N:
            if matrix[current][i] == 1:
                cnt += 1
                if cnt == K and current == N - 1:
                    sum += 1
            else:
                if cnt == K:
                    sum += 1
                cnt = 0
            current+=1

    print('#{} {}'.format(tc, sum))