def factory(cur,sum):
    global minV
    if cur == N:
        if sum < minV:
            minV = sum
        return
    else:
        if sum> minV:
            return
        else:
            for i in range(1,N+1):
                if v[i]==0:
                    v[i]=1
                    factory(cur+1,sum+mtx[cur][i-1])
                    v[i]=0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(N)]
    minV = 100000
    v = [0]*(N+1)
    factory(0,0)
    print('#{} {}'.format(tc,minV))