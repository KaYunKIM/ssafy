T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    max = 0
    min = 1000001
    for i in lst:
        if max < i:
            max = i
        if min > i:
            min= i
    ans = max-min
    print('#{} {}'.format(tc,ans))