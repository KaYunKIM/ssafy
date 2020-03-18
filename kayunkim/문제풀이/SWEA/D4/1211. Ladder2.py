di = [0,0,1]
dj = [1,-1,0]

T = 1
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(100)]
    for j in range(100):
        minV = 9999999999
        cnt = 0
        for i in range(100):
            if mtx[i][j] ==1:
                cnt+=1
                for d in range(3):
                    newi = i+di[d]
                    newj = j+dj[d]

                while newi <100 and 0<= newj< 100:
                    if mtx[newi][newj] ==1:
                        cnt+=1
                        newi+= di[d]
                        newj+=dj[d]
                        if cnt > minV:
                            break
        if minV >= cnt:
            minV = cnt
            ans = i
    print(ans)