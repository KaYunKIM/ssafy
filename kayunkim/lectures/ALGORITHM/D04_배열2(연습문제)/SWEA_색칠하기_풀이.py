def coloring(arr, r1, c1, r2, c2, c):
    for i in range(r1, r2+1)
        for j in range(c1, c2+1):
            if arr[i][j] = 0 or arr[i][j] == c:
                arr[i][j] = c
            else:
                arr[i][j] = 3



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        info = list(map, int(input().split()))
        coloring(arr,info[0],info[1],info[2],info[3],info[4])
        cnt = 0
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                if arr[r][c] == 3:
                    cnt +=1
    print('#{} {}'.format(tc, cnt))

