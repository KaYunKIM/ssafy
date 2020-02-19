T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(N)]
    maxV = 0

    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            sum = 0
            for ii in range(0,M):
                for jj in range(0,M):
                    sum += arr[i+ii][j+jj]
                    print(arr[i+ii][j+jj], end=' ')
            print()

