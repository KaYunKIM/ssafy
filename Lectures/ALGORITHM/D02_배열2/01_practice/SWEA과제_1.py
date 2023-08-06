import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    T = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    max = 0


    for i in range(100):
        sum = 0
        for j in range(100):
            row = matrix[i][j]
            sum+= row
            if max < sum:
                max = sum

    for j in range(100):
        sum = 0
        for i in range(100):
            col = matrix[i][j]
            sum += col
            if max < sum:
                max = sum

    sum = 0
    for i in range(100):
        dr = matrix[i][i]
        sum+= dr
        if max < sum:
            max = sum

    sum = 0
    for i in range(100):
        dl = matrix[i][99-i]
        sum += dl
        if max < sum:
            max = sum

    print('#{} {}'.format(T, max))