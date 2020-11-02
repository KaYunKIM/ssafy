N = int(input())
numbers = list(map(int,input().split()))
temp = []
maxV = -100000
for i in range(N):
    if not temp:
        temp.append(numbers[i])
    else:
        temp = [max(numbers[i],numbers[i]+temp[0])]
    if temp[0] > maxV:
        maxV = temp[0]
print(maxV)