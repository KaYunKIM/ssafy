T = int(input())
for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    stn = list(map(int, input().split()))
    mtx = []
    for i in range(1, N + 1):
        if i in stn:
            mtx.append(1)
        else:
            mtx.append(0)

    ans = [0] + mtx
    cur = 0
    cnt = 0
    while cur < N - K:
        zero = 0
        for n in range(K, 0, -1):
            if ans[cur + n] == 1:
                cnt += 1
                break
            else:
                zero += 1
        if zero == K:
            cnt = 0
            break
        else:
            cur = cur + n
    print('#{} {}'.format(tc, cnt))