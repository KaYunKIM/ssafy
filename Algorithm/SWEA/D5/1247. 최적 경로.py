def distance(k, x1, y1, sumV):
    global minV
    if k == N:
        sumV+= abs(x1-home[0])+abs(y1-home[1])
        if sumV < minV:
            minV = sumV
            return
    else:
        if sumV > minV:
            return
        else:
            for i in range(N):
                if not visited[i]:
                    visited[i] = 1
                    dist = abs(x1-customer[i][0])+abs(y1-customer[i][1])
                    distance(k+1, customer[i][0],customer[i][1], sumV+dist)
                    visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    office = [lst[0], lst[1]]
    home = [lst[2], lst[3]]
    customer = []
    minV = 1000000
    visited = [0]*N
    for i in range(4,len(lst)-1,2):
        customer.append([lst[i], lst[i+1]])
    distance(0, office[0], office[1], 0)
    print('#{} {}'.format(tc,minV))