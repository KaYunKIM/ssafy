T = int(input())
for tc in range(1,T+1):
    N,K = list(map(int,input().split()))
    matrix = [[0]*N for _ in range(4)]

    for i in range(4):
        for j in range(N):

            h = 1
            while h<= K:
                if (i+j+1)%h == 0:
                    if matrix[i][j] == 0:
                        matrix[i][j] =1
                    else:
                        matrix[i][j] = 0
                h+=1
    sum = 0
    for k in matrix:
        sum += k.count(1)
    print(sum)