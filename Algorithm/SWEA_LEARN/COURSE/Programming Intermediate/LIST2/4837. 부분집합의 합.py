T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    mtx = [i for i in range(1, 13)]

    sub = []
    for i in range(1 << 12):
        bin = []
        for j in range(12):
            if i & (1 << j):
                bin.append(mtx[j])
        sub.append(bin)

    ans = []
    for i in sub:
        if len(i) == N and sum(i) == K:
            ans.append(i)
    print('#{} {}'.format(tc, len(ans)))


#실패 => TestCase 10개 중 4개 오류
T = int(input())
for tc in range(1,T+1):
    N,K = list(map(int,input().split()))
    mtx = [i for i in range(1,13)]

    bin1 = []
    for i in range(1<<N):      #전체 집합의 개수 설정 필요!!
        bin = []
        for j in range(13):    #동일하게 12로 설정해야함
            if i&(1<<j):
                bin.append(mtx[j])
        bin1.append(bin)

    cnt = 0
    for i in bin1:
        sum = 0
        if len(i) == N:
            for j in range(len(i)):
                sum+= i[j]
            if sum == K:
                cnt +=1
    print('#{} {}'.format(tc,cnt))