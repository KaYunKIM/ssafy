def find(cur,sumV):
    global minV
    if 0<=sumV-B<minV:
        minV = sumV-B
    if minV ==0:
        return
    if cur==N:
        return
    find(cur+1,sumV+height[cur])
    find(cur+1,sumV)

T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    minV = sum(height)
    find(0,0)
    print('#{} {}'.format(tc,minV))