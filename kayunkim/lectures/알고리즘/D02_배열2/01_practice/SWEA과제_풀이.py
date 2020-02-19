import sys
sys.stdin = open('input.txt', 'r')
T = 10
N = 100

for _ in range(1, T+1):
    tc = int(input())
    arr = [lst(map(int,input().split())) for _ in range(N)]
    max = 0     #최대값을 저장할 변수

    for i in range(N):  #행 우선 반복: 0,0  0,1  0,2
        sum = 0
        for j in range(N):
            sum+= arr[i][j]
        if max < sum:
            max = sum

    for j in range(N):     #열 우선 반복: 0,0  1,0  2,0
        sum = 0
        for i in range(N):
            sum+= arr[i][j]
        if max < sum:
            max = sum

    sum = 0
    for i in range(N):         #대각선 반복: 1,1  2,2  3,3  4,4
        sum+= arr[i][i]
    if max < sum:
        max = sum

    for i in range(N)


    print('#{} {}'.format(tc,max))




