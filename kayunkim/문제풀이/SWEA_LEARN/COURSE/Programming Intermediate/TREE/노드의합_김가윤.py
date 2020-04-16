T = int(input())
for tc in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    node = [0 for i in range(N + 1)]

    for _ in range(M):
        index, num = list(map(int, input().split()))
        node[index] = num
    if N % 2 == 0:
        node[N // 2] = node[N]
        N -= 1
    while N > 1:
        node[N // 2] = node[N] + node[N - 1]
        N -= 2

    print('#{} {}'.format(tc, node[L]))