di = [0,1]
dj = [1,0]

def find(S,G,sumV):
    global minV
    if S == G:
        if sumV < minV:
            minV = sumV
            return
    else:
        if sumV > minV:
            return
        else:
            for d in range(2):
                newi = S[0]+di[d]
                newj = S[1]+dj[d]

                if 0<=newi<N and 0<=newj<N and v[newi][newj]==0:
                    if minV > sumV+int(road[newi][newj]):
                        v[newi][newj]= 1
                        find((newi,newj),G,sumV+int(road[newi][newj]))
                        v[newi][newj]=0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    road = [list(input()) for _ in range(N)]
    minV = float('inf')
    v = [[0]*(N+1) for _ in range(N)]
    find((0,0),(N-1,N-1),0)
    print('#{} {}'.format(tc,minV))