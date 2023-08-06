T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    sum = 0
    for i in range(0,N):
        if i <=N//2:
            for j in range(N//2-i, N//2+i+1):
                sum+= arr[i][j]
        else:
            for j in range(i-N//2, N-(i-N//2)):
                sum += arr[i][j]
    print('#{} {}'.format(tc, sum))
