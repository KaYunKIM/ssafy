def find():
    for i in range(0,10):
        midx = i
        if i%2==0:         # 짝수 인덱스 ->최대값
            for j in range(i+1, N):
                if v[midx] < v[j]:
                    midx = j
        else:                #홀수 인덱스 -> 최소값
            for j in range(i+1,N):
                if v[midx] > v[j]:
                    midx = j
        t = v[i]
        v[i] = v[midx]
        v[midx] = t


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    V = list(map(int,input().split()))
    find()
    print('#{}'.format(tc), end=' ')
    for j in range(0,10):
        print(v[j], end=' ')
    print()