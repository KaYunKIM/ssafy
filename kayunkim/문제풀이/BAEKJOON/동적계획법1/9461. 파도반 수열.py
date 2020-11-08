N = int(input())
for i in range(N):
    num = int(input())
    v = [0] * num
    for i in range(num):
        if i < 3:
            v[i] = 1
        elif i == 3 or i == 4:
            v[i] = 2
        else:
            v[i] = v[i-1]+v[i-5]
    print(v[-1])