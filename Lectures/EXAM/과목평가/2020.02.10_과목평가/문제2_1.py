# T = int(input())
# for tc in range(1, T+1):
#     R,C,N = list(map(int,input().split()))
#     lst = [list(map(int,input().split())) for _ in range(N)]
#     bin = [[0]*C for _ in range(R)]
#
#     for i in range(N):
#         for j in range(lst[i][1]-1,lst[i][3]):
#             for k in range(lst[i][0]-1,lst[i][2]):
#                 bin[k][j] += 1
#
#     maxn = 0
#     for i in range(len(bin)):
#         for j in bin[i]:
#             if maxn < j:
#                 maxn = j
#
#     cnt = 0
#     for k in range(R):
#         for h in range(C):
#             if maxn == bin[k][h]:
#                 cnt+=1
#     print('#{} {}'.format(tc,cnt))

T = int(input())
for tc in range(1,T+1):
    R,C,N = list(map(int,input().split()))
    mtx = [[0] * C for _ in range(R)]
    for _ in range(N):
        r1,c1,r2,c2 = list(map(int,input().split()))
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                mtx[i - 1][j - 1] += 1
    maxV = 0
    for v in mtx:
        for a in range(C):
            if maxV < v[a]:
                maxV = v[a]
    sumV = 0
    for v in mtx:
        sumV += v.count(maxV)
    print('#{} {}'.format(tc, sumV))