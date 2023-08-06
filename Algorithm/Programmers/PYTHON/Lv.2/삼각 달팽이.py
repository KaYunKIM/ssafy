# def solution(n):
#     res = [[0] * n for _ in range(n)]
#     answer = []
#     x, y = -1, 0
#     num = 1
#
#     for i in range(n):
#         for j in range(i, n):
#             if i % 3 == 0:
#                 x += 1
#             elif i % 3 == 1:
#                 y += 1
#             elif i % 3 == 2:
#                 x -= 1
#                 y -= 1
#             res[x][y] = num
#             num += 1
#
#     for i in res:
#         for j in i:
#             if j != 0:
#                 answer.append(j)
#     return answer


def solution(n):
    answer = []
    temp = [[0] * i for i in range(1, n + 1)]
    temp[0][0] = 1

    di = [1, 0, -1]
    dj = [0, 1, -1]
    newi, newj = 0, 0

    ans = 1
    while ans != n * (n + 1) / 2:
        for d in range(3):
            while 0 <= newi < n and 0 <= newj < n:
                if 0 <= newi + di[d] < n and 0 <= newj + dj[d] < n and temp[newi + di[d]][newj + dj[d]] == 0:
                    newi += di[d]
                    newj += dj[d]
                    ans += 1
                    temp[newi][newj] = ans
                else:
                    break

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            answer.append(temp[i][j])

    return answer

solution(4)