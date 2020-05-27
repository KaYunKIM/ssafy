T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
        adj[e][s] = w

    INF = float('inf')
    key = [INF]*(V+1)   #가중치
    MST = [0]*(V+1)

    key[0] = 0    # 0 부터 시작, 가중치 0
    cnt = 0
    result = 0

    while cnt < V+1:
        minV = INF
        u = -1 # 다음 갈 노드 위치
        for i in range(V+1):   #노드 위치 찾기
            if not MST[i] and key[i]<minV:
                minV = key[i]   #도착할 때까지 걸린 거
                u=i
        cnt+=1
        result += minV
        MST[u]=1
        for j in range(V+1):  #갈 수 있는 점과 가중치 업데이트
            if not MST[j] and adj[u][j]>0 and key[j]>adj[u][j]:
                key[j] = adj[u][j]
    print('#{} {}'.format(tc,result))