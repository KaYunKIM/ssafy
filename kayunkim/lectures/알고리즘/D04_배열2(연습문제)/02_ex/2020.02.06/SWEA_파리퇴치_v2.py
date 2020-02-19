#------2X2의 경우일 때----------
T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    matrix = [list(map(int,input().split()))for _ in range(N)]
    n = N-M+1
    bin = []

    for i in range(N-M+M):
        for j in range(n):
            a = matrix[i][j:j+M]
            bin.append(a)
    print(bin)
    print(len(bin))
    maxV = 0
    for k in range(0,len(bin)-N+1):
        sum = 0
        for l in range(M):
            for m in range(M):
                sum += bin[k+m][l+m]
        if maxV < sum:
            maxV = sum
    print('#{} {}'.format(tc,maxV))

# T = int(input())
# for tc in range(1,.)