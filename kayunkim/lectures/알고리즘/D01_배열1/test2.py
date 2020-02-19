# 1   테스트케이스
# 9 8 방크기(9*8)
# 742006070 상자의 높이



T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().split())
    box = list(map(int,input().split()))
    room = [[0 for _ in range(m)] for _ in range(n)]
    print(room)
    for i in range(n):
        for j in range(box[i]):
            room[i][j] = 1
    for row in room:
        print(row)

    max = 0
    for i in range(n):
        if box[i] > 0:
            cnt = 0     #낙차 수 세기
            for j in range(i+1,n):
                if room[i][box[i]] == 0:
                    cnt+=1
            if max < cnt:
                max = cnt
    print(max)



# n = map(int, input().split())
# print(list(n))
#
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)