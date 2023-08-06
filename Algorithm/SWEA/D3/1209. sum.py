T = 10
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(100)]
    mtx += [[mtx[x][y] for x in range(100)] for y in range(100)]
    D1 = []
    D2 = []
    for i in range(100):
        D1.append(mtx[i][i])
    for j in range(100):
        D2.append(mtx[j][99-j])
    mtx= mtx+[D1]+[D2]
    maxV = 0
    for k in range(len(mtx)):
        sum = 0
        for l in range(100):
            sum+= mtx[k][l]
        if maxV < sum:
            maxV = sum
    print('#{} {}'.format(tc,maxV))