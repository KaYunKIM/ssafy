def Game(r,c):
    nr = r -1           #합쳐질 칸 인덱스 (한 칸 위쪽)
    if nr >= 0:         #범위 안이라면
        if maps[nr][c] > 0:         #0보다 크면
            if maps[nr][c] == maps[r][c]:     #서로 같으면
                maps[nr][c] = maps[r][c]*2   #위칸은 *2
                maps[r][c] = -1               #내 칸은 -1
            else:
                return
        elif maps[nr][c] == -1:         #이전에 합쳐져서 -1일 때
            maps[nr][c] = maps[r][c]
            maps[r][c] = 0
            return
        else:                           #0일 때
            maps[nr][c] = maps[r][c]
            maps[r][c] = 0
            Game(nr,c)                  #좌표 변경 후 게임진행

def rotate():
    global maps
    newarr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            newarr[j][N-i-1] = maps[i][j]
    for row in newarr:
        # print(row)
        maps = newarr

T = int(input())
for tc in range(1,T+1):
    N,D = map(str,input().split())
    N = int(N)
    maps = []
    for n in range(N):
        maps.append(list(map(int,input().split())))

    if D == 'up':
        pass
    if D == 'left':
        rotate()
    if D == 'down':
        rotate()
        rotate()
    if D == 'right':
        rotate()
        rotate()
        rotate()

    for r in range(N):
        for c in range(N):      #열 단위로 합치기 진행
            if maps[r][c]:
                Game(r,c)

    #계산에 의해 -1이 되어있는 부분을 0으로
    for r in range(N):
        for c in range(N):
            if maps[r][c] == -1:
                maps[r][c] = 0

    #회전 된 것을 원복시키기
    if D == 'up':
        pass
    if D == 'left':
        rotate()
        rotate()
        rotate()
    if D == 'down':
        rotate()
        rotate()
    if D == 'right':
        rotate()

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str,maps[i])))