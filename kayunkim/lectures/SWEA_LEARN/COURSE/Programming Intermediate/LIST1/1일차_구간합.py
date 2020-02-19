T= int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    max = 0
    min = 10000000000000000000
    for i in range(N-M+1):
        sum = 0
        for j in range(i,i+M):
            sum += lst[j]
        if max < sum:
            max = sum
        if min > sum:
            min = sum
    print('#{} {}'.format(tc,(max-min)))