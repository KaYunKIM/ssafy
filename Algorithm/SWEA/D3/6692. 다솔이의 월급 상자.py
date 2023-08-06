T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans = 0
    for _ in range(N):
        p,q = list((input().split()))
        ans+=float(p)*int(q)
    print('#{} {}'.format(tc,ans))