def maze(row, col):
    stack = [[row, col]]
    mtx[row][col] = '1'

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while stack:
        nrow, ncol = stack.pop()
        if mtx[nrow][ncol] == '3':
            return 1

        for d in range(4):
            newi = nrow + di[d]
            newj = ncol + dj[d]

            if 0 <= newi < N and 0 <= newj < N:
                if mtx[newi][newj] != '1':
                    stack.append([newi, newj])
                    mtx[nrow][ncol] = '1'
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mtx = [list(input()) for _ in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if mtx[i][j] == '2':
                row, col = i, j
                break
    print('#{} {}'.format(tc, maze(row, col)))