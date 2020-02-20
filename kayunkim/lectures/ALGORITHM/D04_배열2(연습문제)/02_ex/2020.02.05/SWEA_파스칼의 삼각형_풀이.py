T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0 for _ in range(N+1)] for _ in range(N)]
    arr[0][1] = 1
    for i in range(1,N):
        for j in range(1,i+2):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print('#{}'.format(tc))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]:
                print(arr[i][j], end='')
        print()