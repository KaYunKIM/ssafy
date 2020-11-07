N = int(input())
v = [0]*(N+1)
for i in range(N+1):
    if i == 0 or i == 1:
        v[i] = i
    else:
        v[i] = v[i-1]+v[i-2]
print(v[-1])