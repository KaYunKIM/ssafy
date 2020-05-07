T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    for i in time:
        i[0],i[1] = i[1], i[0]
    time.sort()
    cnt = 1
    min = 25
    first = time[0][0]
    for i in time:
        if i[1]>= first:
            cnt+=1
            first = i[0]
    print('#{} {}'.format(tc,cnt))


