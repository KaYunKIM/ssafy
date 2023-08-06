T = int(input())
for tc in range(1,T+1):
    N,K = list(map(int,input().split()))
    num = list(map(int,input().split()))
    bin = []
    for i in range(1,N+1):
        if i not in num:
            bin.append(i)
    print('#{} {}'.format(tc,' '.join(map(str,bin))))