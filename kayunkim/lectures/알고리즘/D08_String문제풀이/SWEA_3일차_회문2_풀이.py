def find(row,start,end):
    global ans
    len = end-start+1
    half = len//2 if len%2==0 else len//2+1
    s = []
    for i in range(start,start+half):
        s.append(map[row][i])
    if len%2 == 1:
        s.pop()
    if len != 1:
        for i in range(start+half, end+1):
            if s.pop() != map[row][i]:
                return
    if ans < len:
        ans = len

T = 10
N = 100
for tc in range(1,T+1):
    int(input())
    map = [list(input()) for _ in range(N)]
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(map[j][i])
        map.append(temp)
    ans = 0
    for i in range(200):
        for j in range(100):
            for k in range(j,100):
                if k-j + 1 > ans:
                    find(i,j,k)
    print('#{} {}'.format(tc,ans))