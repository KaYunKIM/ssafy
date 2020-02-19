# T = int(input()) #정원
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     bs = list(map(int, input().split()))
#     bs1 = [0] * (N + 1)
#     for i in bs:
#         bs1[i] = 1
#     cur = 0
#     cnt = 0
#     while cur < N:
#         for k in range(K, 0, -1):
#             if cur + k >= N:
#                 cur = cur + k
#                 break
#             elif bs1[cur + k] == 1:
#                 cnt += 1
#                 cur = cur + k
#                 break
#         else:
#             cnt = 0
#             break
#
#     print('#{} {}'.format(tc, cnt))

T = int(input())
for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    bs = list(map(int, input().split()))
    bs1 = [0] * (N + 1)
    for i in bs:
        bs1[i] = 1

    if K < bs1[0]:
        ans = 0

    cur = 0  # 내위치
    cha = 0
    frag = 0
    count = 0
    while cur <= N:
        for k in range(K, 0, -1):
            if cur + k >= N:
                frag = 1
                break
            if bs1[cur + k] == 1:
                cur += k
                cha += 1
                break
        count += 1
        if frag == 1:
            break
        elif count > N:
            break
    if count < N:
        print('#{} {}'.format(tc, cha))
    else:
        print('#{} 0'.format(tc))