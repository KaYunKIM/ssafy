T  = int(input())
for tc in range(1,T+1):
    N,K = list(map(int,input().split()))
    A = []
    for i in range(1,13):
        A.append(i)
    n = len(A)
    for i in range(1<<n):
        for j in range(n):
            sub = i & (1<<j)
            print(sub)


    # for i in range(1<<3):
    #     for j in range(3):
    #         t = i&(1<<j)
    #         if t != 0:
    #             print(lst[j], end =' ')
