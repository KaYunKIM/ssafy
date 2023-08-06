T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        arr[s][e] = w

    INF = float('inf')
    key = [INF]*(V+1)
    MST = [0]*(V+1)

    key[0] = 0
    cnt = 0
    while cnt < V+1:
        minV = INF
        u = -1
        for i in range(V+1):
            if not MST[i] and key[i] < minV:
                minV = key[i]
                u = i
        MST[u] = 1
        cnt+=1
        for j in range(V+1):
            if not MST[j] and arr[u][j] > 0 and key[j] > arr[u][j]+key[u]:
                key[j] = arr[u][j]+key[u]
    print('#{} {}'.format(tc,key[j]))