T = int(input())
for tc in range(1,T+1):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    matrix = [list(map(int,input().split())) for _ in range(10)]

    r1 = A[0]
    c1 = A[1]
    r2 = A[2]
    c2 = A[3]

    sum_A = 0
    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            a= matrix[x][y] * 2
            if a > 255:
                a = 255
            sum_A += a- matrix[x][y]

    r1 = B[0]
    c1 = B[1]
    r2 = B[2]
    c2 = B[3]

    sum_B = 0
    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            b = matrix[x][y]//2
            sum_B += matrix[x][y] -b
    print('#{} {}'.format(tc,sum_A + sum_B))

