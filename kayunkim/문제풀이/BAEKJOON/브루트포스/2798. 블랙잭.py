N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort(reverse=True)
maxV = 0
for i in range(N-2):
    bin = []
    check = M
    check -= num[i]
    for j in range(i+1,N-1):
        bin = [num[i]]
        if check >= num[j]+num[-1]:
            bin.append(num[j])
            check -= num[j]
            for k in range(j+1,N):
                if check >= num[k]:
                    bin.append(num[k])
                    break
            if sum(bin) > maxV:
                maxV = sum(bin)
            check += num[j]
print(maxV)