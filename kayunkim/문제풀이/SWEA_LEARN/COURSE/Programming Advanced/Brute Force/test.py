def find(num,cur,sumV):
    global minV
    if num == N:    # 한 줄기 끝
        sumV += e[cur][0]
        if sumV < minV:
            minV = sumV
        return
    elif minV <= sumV:   # 한 줄기 내려가는 과정 =>
        return              #줄기 종료
    else:    # 한 줄기 내려가는 과정 중에 아직 최소값을 도달하지 못했을 때
        for i in range(1,N):
            if v[i]==0:
                v[i]=1
                print('i1: {}, num: {}'.format(i+1, num))
                print(v)
                find(num+1, i, sumV+e[cur][i])
                print('i2: {}, num: {}'.format(i+1, num))
                v[i]=0
                print(v)
        return

#
#         0 1 2 3
#    v = [0,0,1,0]
#    1231
#    지금:2
#     가야하는 곳: 1321
#        12
# 321

    # 우리세상                     딴세상1                딴세상2
    # i=1                       find()
    #                             ...
    # i=2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e= [list(map(int,input().split())) for _ in range(N)]
    minV = 10000000000
    v = [0] * (N + 1)
    v[0] = 1
    find(1,0,0)
    print('#{} {}'.format(tc,minV))
