T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    for _ in range(N):
        seats = list(map(int,input().split()))
        cnt+=seats[1]-seats[0]+1
    print('#{} {}'.format(tc,cnt))