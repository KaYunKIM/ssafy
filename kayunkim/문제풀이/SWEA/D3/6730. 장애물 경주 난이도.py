T = int(input())
for tc in range(1,T+1):
    N = int(input())
    block = list(map(int,input().split()))
    maxup = 0
    maxdown = 0
    for i in range(N-1):
        if block[i] <block[i+1]:
            if maxup < block[i+1]-block[i]:
                maxup = block[i+1]-block[i]
        elif block[i] > block[i+1]:
            if maxdown < block[i]-block[i+1]:
                maxdown = block[i]-block[i+1]
    print('#{} {} {}'.format(tc,maxup,maxdown))