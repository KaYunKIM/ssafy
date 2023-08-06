def find():
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    #스택
    s = []
    s.append([sr,sc])
    arr[sr][sc] = 1
    while len(s) != 0:
        n = s.pop()
        for i in range(4):
            nr = n[0] + dr[i]
            nc = n[1] + dc[i]
            if nr >= 0 and nr < N and nc >=0 and nc < N:
                if arr[nr][nc] == 3:
                    return 1
                elif arr[nr][nc] == 0:
                    s.append([nr,nc])
                    arr[n[0]n[1]] = 1   #방문했다고 표시하기 위해 1로 변경
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr= [[int(x) for x in input()] for _ in range(N)]
    for i in range(N):
        if 2 in arr[i]:
            sr = i
            sc = arr[i].index(2)