T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    a = N-M
    b = M-a
    print('#{} {} {}'.format(tc,b,a))