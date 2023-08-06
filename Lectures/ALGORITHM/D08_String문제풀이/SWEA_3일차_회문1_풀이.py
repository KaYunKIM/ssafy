def find():
    global cnt
    s = []
    for i in range(16):         #배열이 2배가 되었으므로 8*2
        for j in range(8-N+1):  #회문 탐색 시작점 설정
            len = 0             #회문 길이 저장

            #짝수면 회문길이/2, 홀수면 회문길이/2+1
            half = N//2 if N%2==0 else N//2+1
            for k in range(half):       #회문의 반절을  s에 담기
                s.append(map[i][j+k])
            if N%2==1:                  #탐색하는 글자 수가 홀수라면
                s.pop()
                len =1
            for k in range(N//2):
                if s.pop() == map[i][j+half+k]:
                    len+=1
    return len

T =10
for tc in range(1,T+1):
    N = int(input())
    map = [list(input()) for _ in range(8)]
    #세로 방향 확인을 위해 열 우선순회해서 배열에 이어붙이기
    for i in range(8):
        temp = []
        for j in range(8):
            temp.append(map[j][i])
        map.append(temp)
    cnt = 0
    print(find())