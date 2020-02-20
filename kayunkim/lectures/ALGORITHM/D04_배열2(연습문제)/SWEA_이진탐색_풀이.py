def find(total, p):
    i = 1       #탐색구간 시작
    r = total   #탐색구간 끝
    cnt =1
    c = int(r+l)/2)
    while c != p:   #중간페이지가 찾을 페이지가 아니라면 반복
        if c < p:   #찾을페이지가 오른쪽에
            ㅣ = c  #시작점 l을 중간페이지로
        else:       #왼쪽에
            r = c   #끝점 r을 중간페이지
        cnt+=1
        c = int((r+l)/2)    #중간페이지 갱신
    return cnt


T = int(input())
for tc in range(1, T+1):
    P,Pa,Pb = map(int,input().split())
    ra = find(P,Pa)
    rb = find(P,Pb)
    result = '0'
    if ra < rb:
        result = 'A'
    elif ra > rb:
        result = 'B'
    print('#{} {}'format(tc,result))
