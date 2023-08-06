def find(n,m):
    maxV = 0
    minV = 100000000  #제한조건으로 계산
    for i in range(0,n-m+1):
        s = 0         #구간의 누적합
        for j in range(i, i+m):
            s = s+v[j]
        if s> maxV:
            maxV = s
        if s < minV:
            minV = s
    return maxV-minV


T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    v = list(map(int,input().split()))
    print('#{} {}'.format(tc, find(N,M)))


