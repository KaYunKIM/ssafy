T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    bin = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans = list(str(num[i] * num[j]))
            for k in range(len(ans) - 1):
                if ans[k] > ans[k + 1]:
                    break
            else:
                bin.append(num[i] * num[j])

    if len(bin) != 0:
        maxV = 0
        for i in bin:
            if maxV < i:
                maxV = i
        print('#{} {}'.format(tc, maxV))
    else:
        print('#{} -1'.format(tc))


#시간초과
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    bin = []
    for i in range(0,N-1):
        for j in range(i+1,N):
            new = str(num[i]*num[j])
            nmax = 0
            for k in new:
                if nmax <= int(k):
                    nmax = int(k)
                else:
                    break
            if nmax == int(new[-1]):
                bin.append(int(new))
    if len(bin) !=0:
        maxV = 0
        for i in bin:
            if maxV < i:
                maxV = i
        print('#{} {}'.format(tc,maxV))
    else:
        print('#{} -1'.format(tc))