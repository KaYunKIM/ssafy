di = [0,1,0,-1]
dj = [1,0,-1,0]

def fill(i,j):
    global N
    cnt = 1
    while cnt <= N*N:
        for d in range(4):
            newi = i + di[d]
            newj = j + dj[d]

            while newi< N and newj <N:
                if array[newi][newj]:
                    break
                else:
                    array[newi][newj] = cnt
                    cnt+=1
                newi+=di[d]
                newj+=dj[d]
            i, j = newi-di[d], newj-dj[d]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [[0]*N for _ in range(N)]
    fill(0,-1)
    print('#{}'.format(tc))
    for i in array:
        print(' '.join(map(str,i)))