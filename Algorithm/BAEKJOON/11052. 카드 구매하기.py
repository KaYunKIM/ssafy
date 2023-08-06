# 시간초과
def find(cur, sumV):
    global maxV

    if cur == N:
        if sumV > maxV:
            maxV = sumV
        return

    for i in range(N):
        if cur + i <= N:
            find(cur+i+1, sumV + price[i])

N = int(input())
price = list(map(int,input().split()))

maxV = 0
find(0,0)
print(maxV)


N = int(input())
price = list(map(int,input().split()))
price.insert(0,0)

for i in range(1,N+1):
    temp = set()
    for j in range(1,i+1):
        temp.add(price[j]+price[i-j])
    price[i] = max(temp)

print(price[-1])