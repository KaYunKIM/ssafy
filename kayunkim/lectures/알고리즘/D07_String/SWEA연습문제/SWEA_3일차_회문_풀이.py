def find():
    for i in range(N):
        for j in range(N-M+1):
            k = 0         #가로찾기
            h = M//2
            while k < h:
                if s[i][j+k] != s[i][j+M-k-1]:
                    break
                k+=1
            if k == h:          #회문 찾음
                print(s[i][j:j+M])
                return      #회문은 1개니까 찾으면 바로 리턴
            k = 0           #세로찾기
            while k < h:
                if s[j+k][i] != s[j+M-k-1][i]:
                    break
                k+=1
            if k == h:
                for ii in range(j,j+M):
                    print(s[ii][i], end='')
                print()
                return

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    s = [input() for i in range(N)]     #문자열 입력받아서 2차원으로
    print('#{}'.format(tc), end=' ')
    find()