def sorM(i):
    maxV = 0
    for i in lst:
        if maxV < i:
            maxV = i
        lst.remove(i)
    return maxV


def sorm(i):
    minV = 101
    for i in lst:
        if minV > i:
            minV = i
        lst.remove(i)
    return minV


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    for i in lst:
        print(sorM(i))
        # print(sorm(i))
    # bin = []
    # bin.append(sorM(i))
    # bin.append(sor(i))
    # print(bin)

