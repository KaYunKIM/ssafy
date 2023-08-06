for tc in range(1,11):
    N = int(input())
    magnet = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        bin = []
        for j in range(N):
            if magnet[j][i] == 1:
                bin.append(1)
            elif magnet[j][i] == 2 and bin:
                cnt+=1
                bin = []
    print('#{} {}'.format(tc,cnt))