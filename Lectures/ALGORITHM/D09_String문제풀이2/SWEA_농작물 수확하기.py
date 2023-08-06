T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    sum = 0
    a = N // 2
    for i in range(N):
        if i <= a:
            for j in range(a - i, N - (a - i)):
                sum += int(matrix[i][j])
        else:
            for j in range(i - a, N - (i - a)):
                sum += int(matrix[i][j])
    print('#{} {}'.format(tc, sum))

