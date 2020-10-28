N = int(input())
find = [0]*(N+1)
for i in range(2, N+1):
    temp = []
    if i%3 == 0:
        temp.append(find[i//3]+1)
    if i%2 == 0:
        temp.append(find[i//2]+1)
    temp.append(find[i-1]+1)
    find[i] = min(temp)
print(find[-1])