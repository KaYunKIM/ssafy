N = int(input())
wine = [int(input()) for _ in range(N)]
check = [[1,1,0], [1,0,1], [0,1,1]]
maxV = []
for i in range(N):
    if i <2:
        maxV.append(sum(wine[:i+1]))
    elif i==2:
        maxV.append(max(maxV[-1], maxV[-2]+wine[i], wine[i-1]+wine[i]))
    else:
        temp = []
        temp.append(maxV[-1])
        temp.append(maxV[-2]+wine[i])
        temp.append(maxV[-3]+wine[i-1]+wine[i])
        maxV.append(max(temp))
print(maxV[-1])