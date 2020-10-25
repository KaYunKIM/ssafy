N = int(input())
maxV = [0]*N
step = [int(input()) for i in range(N)]
for i in range(N):
    if i<2:
        maxV[i] = step[i]+sum(maxV)
    elif i == 2:
        maxV[i] = max(step[i-1]+step[i],maxV[i-2]+step[i])
    else:
        temp = []
        temp.append(maxV[i-3]+step[i-1]+step[i])
        temp.append(maxV[i-2]+step[i])
        maxV[i] = max(temp)
print(maxV[-1])