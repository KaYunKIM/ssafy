T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int,input().split())) for _ in range(100)]
    max_v = 0
    sum_h = 0
    sum_diag = 0

    vertical = []
    height = []

    for i in range(len(matrix)):
        vertical.append(matrix[i])
        if max_v < int(matrix[i]):
            max_v = matrix[i]
        print(max_v)
    # for j in range(len(matrix[i])):
    #     print(j)
    #     sum_v += matrix[i][j]
    #         vertical.append(sum_v)
    # print(vertical)




    # for j in range(len(matrix)):
    #     for i in range(len(matrix(j))):
    #         sum_h += matrix[i][j]
    #         MH = max(sum_h)
    # for diag in range(len(matrix)):
    #     sum_diag += matrix[diag][diag]
    #     MD = max(sum_diag)
    #



