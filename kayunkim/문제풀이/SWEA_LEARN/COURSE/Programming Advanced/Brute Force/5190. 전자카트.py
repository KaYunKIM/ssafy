def find(num,cur,sumV):
    global minV
    if num==N:
        sumV+=e[cur][0]
        if minV > sumV:
            minV = sumV
            return
    elif minV <= sumV:
        return
    else:
        for i in range(1,N):
            if v[i]==0:
                v[i]=1
                find(num+1,i,sumV+e[cur][i])
                v[i]=0
        return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e = [list(map(int,input().split())) for _ in range(N)]
    minV = 10000000
    v= [0]*(N+1)
    find(1,0,0)
    print('#{} {}'.format(tc,minV))