T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    tot = 0
    for i in range(N):
        for j in range(N-1):
            if matrix[i][j] == 1:
                cnt+= 1
                if cnt == K:
                    if matrix[i][j+1] == 1:
                        cnt = 0
                    else:
                        tot+=1
                        cnt = 0
                if cnt < K:
                    if matrix[i][j] == matrix[i][-2]:
                        if cnt == K-1:
                            if matrix[i][-1] == 1:
                                tot+= 1
                                cnt = 0
                            else:
                                cnt = 0
                    else:
                        cnt = 0
            else:
                cnt = 0

    print('#{} {}'.format(tc, tot))


# elif cnt < K:
# if cnt == K - 1:
#     if matrix[i][j + 1] == 1:
#         tot += 1
#         cnt = 0
#     else:
#         cnt = 0
# else:
#     cnt = 0