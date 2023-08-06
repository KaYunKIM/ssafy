T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    BM = [[0]*10 for _ in range(10)]

    for n in range(N):
        for i in range(matrix[n][0], matrix[n][2]+1):
            for j in range(matrix[n][1], matrix[n][3]+1):
                BM[i][j] += 1

    cnt = 0
    for i in range(len(BM)):
        for j in range(len(BM)):
            if BM[i][j] == 2:
                cnt+=1
    print('#{} {}'.format(tc,cnt))
