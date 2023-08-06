import heapq

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        arr[s][e] = w
        arr[e][s] = w

    INF = float('inf')
    key= [INF]*(V+1)
    MST = [0]*(V+1)

    pq = []
    heapq.heappush(pq,(0,0))  #(w,e)
    result = 0
    while pq:
        w,e = heapq.heappop(pq)
        if MST[e]:
            continue
        else:
            result+=w
            MST[e]=1
            for idx,val in enumerate(arr[e]):
                if not MST[idx] and val >0 and key[idx] > val:
                    key[idx] =val
                    heapq.heappush(pq,(val,idx))
            # for dest in range(V+1):
            #     if not MST[dest] and arr[e][dest]>0 and key[dest] > arr[e][dest]:

    print('#{} {}'.format(tc,result))