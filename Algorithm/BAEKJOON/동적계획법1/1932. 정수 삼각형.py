N = int(input())
pyramid = [list(map(int,input().split())) for _ in range(N)]
maxV = pyramid[0][0]
for i in range(1,N):
    for j in range(len(pyramid[i])):
        if j == 0:
            pyramid[i][j]+=pyramid[i-1][j]
        elif j == len(pyramid[i])-1:
            pyramid[i][j]+=pyramid[i-1][j-1]
        else:
            pyramid[i][j]+= max(pyramid[i-1][j-1], pyramid[i-1][j])
print(max(pyramid[-1]))