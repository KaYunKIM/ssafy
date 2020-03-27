T = int(input())
for tc in range(1,T+1):
    a1,a2,a3,a4 = list(map(int,input().split()))
    b1,b2,b3,b4 = list(map(int,input().split()))
    mtx = [list(map(int,input().split())) for _ in range(10)]
    suma = 0
    sumb = 0
    for i in range(a1,a3+1):
        for j in range(a2,a4+1):
            ans = mtx[i][j]*2
            if ans >= 255:
                ans = 255
            suma+= ans-mtx[i][j]

    for i in range(b1,b3+1):
        for j in range(b2,b4+1):
            ans = mtx[i][j]//2
            sumb+= mtx[i][j]-ans
    print('#{} {}'.format(tc,suma+sumb))