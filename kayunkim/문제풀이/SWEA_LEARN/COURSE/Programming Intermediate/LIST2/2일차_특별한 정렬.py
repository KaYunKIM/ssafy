T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    maxV = 0
    minV = 101
    bin = []
    for j in lst:
        for i in lst:
            if maxV < i:
                maxV = i
            lst.remove(maxV)
        bin.append(maxV)
        print(lst)


        # for i in lst:
        #     if minV > i:
        #         minV = i
        # bin.append(minV)
        # lst.remove(minV)

    print(bin)

