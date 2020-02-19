def search(r,c):
    #왼,오른,아래 탐색
    dr = [0,0,1]
    dc = [1,-1,0]
    visited = [[for i in range(N)] for j in range(N)] #방문배열 초기화
    num = arr[r][c]
    cnt = 0

    while True:
        if r == 99: return cnt      #99행까지 왔으면 cnt리턴
        for k in range(3):
            nr = r + dr[k]          #왼,오,아래 중 갈 수 있는 길 찾기
            nc = c + dc[k]          #새로운 좌표를 검증하기 위한 계산

            #새로운 좌표가 사다리 안인지, 이미 방문했는지, 사다리인지
            if nr < 0 or nr >= N or nc < 0 or nc >=N: continue
            if visited[nr][nc] == 1: continue
            if arr[nr][nc] == 0: continue


        #새로 찾은 좌표로 갱신, 방문했다고 표시
        r = nr
        c = nc
        visited[nr][nc] = 1
        num = arr[nr][nc]
        cnt += 1       #칸 수 세어가기
        break

T = 10
for tc in range(1, T+1):
    t = int(input())
    N =100
    arr = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        if arr[0][i] == 1:
            #시작점에서부터 탐색 시작
            cnt = search(0,i)       #시작점 -> 사다리타고 -> 99행까지 도착 -> 지나온 거리
            if ans > cnt:
                ans = cnt
                minidx = i
    print('#{} {}'.format())
