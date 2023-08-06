for tc in range(1,11):
    N = int(input())
    mtx = [list(input()) for _ in range(100)]
    mtx += [[mtx[x][y] for x in range(100)] for y in range(100)]
    max = 0
    for i in range(200):
        for j in range(100):
            for k in range(1,100-j+1):
                if mtx[i][j:j+k] == mtx[i][j+k-1:j-1:-1]:
                    if max< len(mtx[i][j:j+k]):
                        max = len(mtx[i][j:j+k])

    print(max)

