def binary(N):
    cnt = 0
    bin = ''
    while True:
        bin+= str(int(N*2))
        N = N*2 - int(N*2)
        cnt+=1
        if N == 0.0:
            return bin
        if cnt> 13:
            return 'overflow'

T = int(input())
for tc in range(1,T+1):
    N = float(input())
    print('#{} {}'.format(tc,binary(N)))