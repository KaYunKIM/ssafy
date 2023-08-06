T = int(input())
for tc in range(1,T+1):
    N = int(input())
    income = list(map(int,input().split()))
    income_avg = sum(income)//N
    cnt = 0
    for i in income:
        if i <= income_avg:
            cnt+=1
    print('#{} {}'.format(tc,cnt))