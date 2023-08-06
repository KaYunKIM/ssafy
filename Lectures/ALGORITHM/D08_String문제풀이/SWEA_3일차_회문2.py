T = 10
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(100)]
    matrix += [[matrix[x][y] for x in range(100)] for y in range(100)]

    max = 0
    for i in range(200):
        for j in range(100):
            for k in range(1, 100 - j + 1):
                if matrix[i][j:j + k] == list(reversed(matrix[i][j:j + k])):
                    if max < len(list(matrix[i][j:j + k])):
                        max = len(list(matrix[i][j:j + k]))
    print('#{} {}'.format(tc, max))