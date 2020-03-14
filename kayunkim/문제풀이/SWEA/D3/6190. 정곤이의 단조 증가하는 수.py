def dan(N):
    T = N%10
    N = N//10
    while N!=0:
        if N%10 > T:
            return False
        T = N%10
        N = N//10
    return True

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    ans = -1
    for i in range(N):
        for j in range(i+1,N):
            if ans < num[i]*num[j]:
                if dan(num[i]*num[j]):
                    ans = num[i]*num[j]
    print('#{} {}'.format(tc,ans))


시간초과
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    bin = []
    for i in num:
        maxV = 0
        for j in range(len(str(i))):
            if maxV <= int(str(i)[j]):
                maxV = int(str(i)[j])
        if maxV == int(str(i)[-1]):
            bin.append(i)
    if len(bin) == 0:
        print('#{} {}'.format(tc,'-1'))
    else:
        maxV = 0
        for i in range(0,len(bin)-1):
            for j in range(i+1,len(bin)):
                if maxV < bin[i]*bin[j]:
                    maxV = bin[i]*bin[j]
        print('#{} {}'.format(tc,maxV))