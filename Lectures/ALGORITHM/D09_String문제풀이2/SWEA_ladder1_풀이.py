def find(sr,sc):
    #오른쪽, 왼쪽, 위
    dr = [0,0,-1]
    dc = [1,-1,0]

    while True:
        for k in range(3):            #3방향 검사하기
            nr = sr + dr[k]
            nc = sc + dc[k]
            if nr >= 0 and nr < 100 and nc >= 0 and nc < 100:
                if ladder[nr][nc] == 1:
                    break
        if nr == 0:
            return nc
        ladder[nr][nc] = 0      #왔던 길을 다시 돌아가지 않도록 0으로
        sr = nr                 #다음 반복을 위해서 좌표를 갱신
        sc = nc

