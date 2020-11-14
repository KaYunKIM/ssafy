N = int(input())
nc = [[0]*10
for _ in range(inputNum+1)]
ans, mod = 0, 1000000000
for i in range(1, 10):
    nc[1][i] = 1
for i in range(2, inputNum+1):
    for j in range(0, 10):
        if j > 0:
            nc[i][j] += nc[i-1][j-1]
        if j < 9:
            nc[i][j] += nc[i-1][j+1]
        nc[i][j] %= mod
print(sum(nc[inputNum])%mod)