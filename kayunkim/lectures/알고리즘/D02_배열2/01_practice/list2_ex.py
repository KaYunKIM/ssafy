#연습문제
2 7 4 3 6
8 5 8 3 2
2 2 3 6 9
5 9 2 5 7
3 6 2 9 4


# import sys
# sys.stdin = open('input.txt', 'r')

arr = [list(map(int,input().split())) for _ in range(5)]
print(arr)

dr = [-1,0,1,0]
dc = [0,1,0,-1]

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        sum = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nr >= len(arr) or nc < 0 or nc >=len(arr[i]):
                continue
            # print(abs(arr[i][j]-arr[nr][nc]))
            sum = sum + abs(arr[i][j]- arr[nr][nc])
        print(sum, end=' ')
    print()
