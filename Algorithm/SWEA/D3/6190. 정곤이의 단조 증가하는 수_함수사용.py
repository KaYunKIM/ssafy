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