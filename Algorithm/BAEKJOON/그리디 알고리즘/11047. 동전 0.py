N, K = map(int,input().split())
coin = [int(input()) for x in range(N)]
ans = 0
coin_sum = 0
originK = K
for i in range(N-1,-1,-1):
    if coin[i]<= K:
        num = K//coin[i]
        K-= coin[i]*num
        coin_sum+=coin[i]*num
        ans+=num
    if coin_sum == originK:
        break
print(ans)