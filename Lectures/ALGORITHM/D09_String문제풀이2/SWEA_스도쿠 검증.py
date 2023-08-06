T = int(input())
for tc in range(1,T+1):
    matrix = [list(map(int,input().split())) for _ in range(9)]
    matrix += [[matrix[x][y] for x in range(9)] for y in range(9)]

    for i in range(0,9,3):
        for l in range(3):
            bin = []
            for j in range(i,i+3):
                for k in range(l*3,l*3+3):
                    bin.append(matrix[j][k])
            # matrix += [bin]
            matrix.append(bin)

    s = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        for i in range(27):
            max = matrix[i][0]
            for j in range(1,9):
                if max < matrix[i][j]:
                    max = matrix[i][j]
                else:
                    matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]

    for i in range(27):
        if matrix[i] == s:
            ans = 1
        else:
            ans = 0
            break
    print('#{} {}'.format(tc,ans))