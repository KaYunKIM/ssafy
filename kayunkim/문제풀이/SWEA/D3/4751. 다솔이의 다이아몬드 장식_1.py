T = int(input())
for tc in range(1, T + 1):
    lst = list(input())
    n = len(lst) * 4 + 1
    matrix = [['.'] * n for _ in range(5)]
    for i in range(2, n, 4):
        matrix[0][i] = '#'
    for i in range(1, n, 2):
        matrix[1][i] = '#'
    for i in range(0, n, 4):
        matrix[2][i] = '#'
    for i in range(len(lst)):
        matrix[2][i * 4 + 2] = lst[i]
    for i in range(1, n, 2):
        matrix[3][i] = '#'
    for i in range(2, n, 4):
        matrix[4][i] = '#'

    for i in matrix:
        print(''.join(i))