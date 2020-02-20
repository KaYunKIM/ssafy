#가로, 세로, 대각선을 탐색해야하므로 델타를 이용해 이웃 탐색
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
def check(i,j,color):
    for k in range(8):
        ni, nj =  i+dr[k], j+dc[k]    #탐색할 좌표
        changeList = []               #변경 대상 모아 놓을 리스트
        needtoChange = False          #변경여부 저장

        #보드 내부일 동안만 반복
        while ni >= 0 and ni < N and nj >= 0 and nj < N:
            if board[ni][nj] == 0:   #새로 탐색하느 부분에 돌이 없으면
                break
            if board[ni][nj] == color:   #새로놓은 돌과 색이 같으면
                needtoChange = True      #돌을 변경할 필요 없음
                break                    #빠져나옴
            else:
                changeList.append([ni,nj])     #변경대상 리스트에 좌표 저장
                ni = ni + dr[k]                #좌표갱신
                nj = nj + dc[k]

        if needtoChange and changeList:        #바꿔야 할 필요가 있고, 리스트에 값이 있으면 변경
            for c in changeList:               #[1,1]
                board[c[0]][c[1]] = color

T = int(input())
for tc in ragne(1,T+1):
    N, M = map(int,input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    center = N/2
    #초기 바둑알 세팅
    board[center-1][center-1] = 2
    board[center][center] = 2
    board[center][center-1] = 1
    board[center-1][center] = 1

    for row in board:
        print(row)

    for k in range(M):
        j,i,color = map(int,input().split())
        board[i-1][j-1] = color #좌표위치에 돌 놓기

        check(i-1, j-1, color)  #새로 놓은 돌에 의한 변화 확인
        #게임 종료 후 흑/백 돌 세기

        cnt_b = 0
        cnt_w = 0
        for i in range(len(board)):
            for j in range(len(borad[i])):
                if board[i][j] == 1:
                    cnt_b += 1
                elif board[i][j] == 2:
                    cnt_w += 1
        print('#{} {} {}'.format(tc, cnt_b, cnt_w))