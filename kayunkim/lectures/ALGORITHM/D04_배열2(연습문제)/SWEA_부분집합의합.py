T = int(input())
matrix = []
for i in range(1,13):
    matrix.append(i)
# matrix = [i for i in range(1,13)]
n = len(matrix)



for tc in range(1, T+1):
    N, K = map(int,input().split())
    result = 0

    for i in range(1 << n):
        sum = 0
        cnt = 0
        for j in range(n):
            if i & (1 << j):
                sum += matrix[j]
                cnt += 1
        if cnt == N and sum == K:
            result += 1
    print('#{} {}'.format(tc, result))

