T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    zero = [0,0,0,1,1,0,1]
    one = [0,0,1,1,0,0,1]
    two = [0,0,1,0,0,1,1]
    three = [0,1,1,1,1,0,1]
    four = [0,1,0,0,0,1,1]
    five = [0,1,1,0,0,0,1]
    six = [0,1,0,1,1,1,1]
    seven = [0,1,1,1,0,1,1]
    eight = [0,1,1,0,1,1,1]
    nine = [0,0,0,1,0,1,1]
    bin = [0]*8
    ans = 0
    mtx = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(M-1,6,-1):
            if mtx[i][j] == 1:
                cnt = 7
                for k in range(j,j-56+1,-7):
                    if mtx[i][k-6:k+1] == zero:
                        bin[cnt] = 0
                    elif mtx[i][k-6:k+1] == one:
                        bin[cnt] = 1
                    elif mtx[i][k-6:k+1] == two:
                        bin[cnt] = 2
                    elif mtx[i][k-6:k+1] == three:
                        bin[cnt] = 3
                    elif mtx[i][k-6:k+1] == four:
                        bin[cnt] = 4
                    elif mtx[i][k-6:k+1] == five:
                        bin[cnt] = 5
                    elif mtx[i][k-6:k+1] == six:
                        bin[cnt] = 6
                    elif mtx[i][k-6:k+1] == seven:
                        bin[cnt] = 7
                    elif mtx[i][k-6:k+1] == eight:
                        bin[cnt] = 8
                    elif mtx[i][k-6:k+1] == nine:
                        bin[cnt] = 9
                    # else:
                    #     bin[cnt] = 'n'
                    #     break
                    cnt-=1
                # if bin.count('n') == 0:
                if ((bin[0]+bin[2]+bin[4]+bin[6])*3+(bin[1]+bin[3]+bin[5])+bin[7])%10 == 0:
                    ans = sum(bin)
                break
    print('#{} {}'.format(tc,ans))