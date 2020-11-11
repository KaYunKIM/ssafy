N,K = map(int,input().split())
bag = [list(map(int,input().split())) for _ in range(N)]
maxV = [0]*N
weight = [0]*N
for i in range(N):
    if i == 0:
        weight[i] = bag[i][0]
        maxV[i] = bag[i][1]
    else:
        if maxV[-1]+bag[i][0] <= K:
            w = maxV[-1]+bag[i][0]
            m = maxV[-1] + bag[i][1]
        else:
            if i == 1:
                w = max(weight[-1])
                maxV[i] = maxV[-1]
            else:
                w = max(weight[-1])
                maxV[i] = maxV[-1]