N = int(input())
binz = {}
bino = {}
for i in range(N):
    num = int(input())
    for i in range(num+1):
        if i == 0 :
            binz[i] = 1
            bino[i] = 0
        elif i == 1:
            bino[i] = 1
            binz[i] = 0
        else:
            binz[i] = binz[i-1]+binz[i-2]
            bino[i] = bino[i-1]+bino[i-2]
    print(binz[num], bino[num])