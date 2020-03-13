T = int(input())
for tc in range(1,T+1):
    N = input()
    M = input()
    bin = {}
    for i in N:
        if i not in bin:
            for j in M:
                if i in j:
                    if i not in bin:
                        bin[i]=1
                    else:
                        bin[i]+=1
    maxV = 0
    for i in bin:
        if maxV < bin[i]:
            maxV = bin[i]
    print('#{} {}'.format(tc,maxV))


#함수사용
def f(N,M):
    global maxV
    for i in N:
        if i not in bin:
            for j in M:
                if i in j:
                    if i not in bin:
                        bin[i]=1
                    else:
                        bin[i]+=1
    for i in bin:
        if maxV < bin[i]:
            maxV = bin[i]
    return maxV

T = int(input())
for tc in range(1,T+1):
    N = input()
    M = input()
    bin = {}
    maxV = 0
    print('#{} {}'.format(tc,f(N,M)))
