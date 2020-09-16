N = input()
minV = 100000000
if len(N)==1:
    print('0')
else:
    for i in range(int(N)-1,int(N)//2,-1):
        sumV = i
        for j in range(len(str(i))):
            sumV+=int(str(i)[j])
            if sumV >int(N):
                break
        if sumV == int(N) and i < minV:
            minV = i
    if minV == 100000000:
        print('0')
    else:
        print(minV)