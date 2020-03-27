T = int(input())
for tc in range(1,T+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    sum = 0
    for i in range(N):
        for j in range(abs(N//2-i),N-abs(N//2-i)):
            sum+= int(farm[i][j])
    print(sum)