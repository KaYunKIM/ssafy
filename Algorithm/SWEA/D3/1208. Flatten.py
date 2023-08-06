T = 1
for tc in range(1,T+1):
    N = int(input())
    BOX = list(map(int,input().split()))
    for _ in range(N):
        maxV = 0
        minV = 101
        for i,j in enumerate(BOX):
            if maxV < j:
                maxV = j
                maxidx = i
            if minV > j:
                minV = j
                minidx = i
        BOX[maxidx]-=1
        BOX[minidx]+=1
        print(BOX[maxidx],BOX[minidx])
    print('#{} {}'.format(tc,max(BOX)-min(BOX)))


#2번째 풀이
T = 10
for tc in range(1,T+1):
    N = int(input())
    box = list(map(int,input().split()))
    for i in range(N):
        box[box.index(max(box))]-=1
        box[box.index(min(box))]+=1
    print('#{} {}'.format(tc,max(box)-min(box)))