def ladder(i, j):
    cnt = 1
    visited = [[0] * 100 for _ in range(100)]

    while True:
        if i == 99:
            return cnt
        else:
            di = [0, 0, 1]
            dj = [-1, 1, 0]

            for d in range(3):
                newi = i + di[d]
                newj = j + dj[d]

                if 0 <= newi < 100 and 0 <= newj < 100:
                    if mtx[newi][newj] == 1 and visited[newi][newj] == 0:
                        i, j = newi, newj
                        visited[newi][newj] = 1
                        cnt += 1
                        break


T = 10
for tc in range(1, T + 1):
    N = int(input())
    mtx = [list(map(int, input().split())) for _ in range(100)]
    minV = 9999999999
    for k in range(100):
        if mtx[0][k] == 1:
            ans = ladder(0, k)
            if minV > ans:
                minV = ans
                idx = k
    print('#{} {}'.format(tc, idx))