T = 10
for tc in range(1,T+1):
    N = int(input())
    BD = list(map(int,input().split()))
    cnt = 0
    for i in range(2,N-2):
        maxV = max(BD[i-2],BD[i-1],BD[i+1],BD[i+2])
        if BD[i]> maxV:
            cnt+=BD[i]-maxV
    print('#{} {}'.format(tc,cnt))