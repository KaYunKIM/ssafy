di = [-1,0,1,0]
dj = [0,1,0,-1]

T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    matrix = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(M):
            k = matrix[i][j]
            sum = k

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                h = 1
                while 0<= ni < N and 0 <= nj < M and h<= k:
                    sum+= matrix[ni][nj]
                    ni += di[d]
                    nj +=  dj[d]
                    h += 1
            if maxV < sum:
                maxV = sum

    print('#{} {}'.format(tc,maxV))