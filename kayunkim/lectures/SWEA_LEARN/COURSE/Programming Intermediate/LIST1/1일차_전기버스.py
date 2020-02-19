T = int(input())
for tc in range(1,T+1):
    K,N,M = list(map(int,input().split()))
    bs = list(map(int,input().split()))
    bs1 = [0]*(N+1)
    for i in bs:
        bs1[i] = 1
    print(bs1)

    if K < bs1[0]:
        ans = 0

    cur = 0      #내위치
    cha = 0
    while cur <= N:
        for k in range(K,0,-1):
            if bs1[cur+k] == 1:
                cur = cur + k
                print('cur', cur)
                if cur + k <= N:
                    cha+=1
                    print('cha', cha)

            if cur + k >= N:
                break
        break
