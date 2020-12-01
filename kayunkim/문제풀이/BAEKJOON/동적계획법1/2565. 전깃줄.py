N = int(input())
pole = []
poleMaxV = 0
for _ in range(N):
    A,B = map(int,input().split())
    if B > poleMaxV:
        poleMaxV = B
    pole.append([A,B])
pole.sort()
LIS = [0]*(poleMaxV+1)
ans = 0
for i in pole:
    maxV = 0
    for j in range(1,i[1]+1):
        if LIS[j] > maxV:
            maxV = LIS[j]
    LIS[i[1]] = maxV+1
    if LIS[i[1]] > ans:
        ans = LIS[i[1]]
print(N-ans)