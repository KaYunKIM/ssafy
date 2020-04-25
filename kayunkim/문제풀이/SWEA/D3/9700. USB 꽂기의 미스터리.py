T= int(input())
for tc in range(1,T+1):
    ans = 'NO'
    p,q = list(map(float,input().split()))
    if (1-p)*q < p*(1-q)*q:
        ans = 'YES'
    print('#{} {}'.format(tc,ans))

    # 0.8  0.5
    # s1 = 0.2*0.5 = 0.1
    # s2 = 0.8*0.5(1번째 시도)*0.5(2번째 시도) = 0.2
    #
    # 0.6  0.5
    # s1 = 0.4*0.5 = 0.2
    # s2 = 0.6*0.5*0.5 = 0.15
