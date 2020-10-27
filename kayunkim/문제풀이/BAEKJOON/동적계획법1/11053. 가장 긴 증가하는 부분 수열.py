N = int(input())
num = list(map(int,input().split()))
cnt = [1]*N
cnt[0] = 1
for i in range(1,N):
    temp = []
    for j in range(0,i):
        if num[j]< num[i]:
            temp.append(cnt[j]+1)
    if temp:
        cnt[i] = max(temp)
print(cnt)