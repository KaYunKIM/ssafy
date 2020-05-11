T = int(input())
for tc in range(1,T+1):
    m,d = list(map(int,input().split()))
    one = [1,3,5,7,8,10,12]
    nine = [2]
    for i in range(1,m):
        if i in one:
            d+=31
        elif i in nine:
            d+=29
        else:
            d+=30
    if d%7 == 4 or d%7 == 5 or d%7 == 6:
        print('#{} {}'.format(tc, (d%7)-4))
    else:
        print('#{} {}'.format(tc, (d%7)+3))