T = int(input())
for tc in range(1,T+1):
    mtx = [list(input()) for _ in range(5)]
    maxV = 0
    for i in mtx:
        if maxV < len(i):
            maxV = len(i)
    bin = []
    for j in range(maxV):
        for i in range(5):
            if j < len(mtx[i]):
                bin.append(mtx[i][j])
    print('#{} {}'.format(tc,''.join(bin)))