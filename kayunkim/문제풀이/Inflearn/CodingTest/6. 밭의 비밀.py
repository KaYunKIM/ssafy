import numpy as np

first = [
    [1,0,0,0,0],
    [0,0,1,0,1],
    [0,0,1,0,1],
    [0,0,1,0,1],
    [0,0,1,0,1]
]

second = [
    [0,0,0,0,1],
    [0,0,0,0,3],
    [0,0,0,0,4],
    [0,2,0,0,2],
    [4,5,0,2,0]
]

sample = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

ans = np.rot90(second,1) + np.array(first)
for i in ans:
    i = list(i)
    i = ''.join(map(str,i))
    print(chr(int(i,8)))




## 행렬덧셈 구하기
# for i in range(len(second)):
#     for j in range(len(second[0])):
#         sample[i][j] = second[j][len(second[0])-i-1]
# print(sample)
#
# for i in range(len(second)):
#     for j in range(len(second[0])):
#         sample[i][j] += first[i][j]
# print(sample)