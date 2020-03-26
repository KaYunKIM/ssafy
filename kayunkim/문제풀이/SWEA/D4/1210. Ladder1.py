# def ladder(row,col,N):
#     stack = [[row,col]]
#
#     di = [0,0,1]
#     dj = [-1,1,0]
#
#     while N != 100:
#         print(stack)
#         nrow,ncol = stack.pop()
#         if mtx[nrow][ncol] == 2:
#             return col
#         else:
#             for d in range(3):
#                 newi = nrow + di[d]
#                 newj = ncol + dj[d]
#                 if 0<= newi<100 and 0<= newj<100:
#                     if mtx[newi][newj] == 1:
#                         stack.append([newi,newj])
#                         newi+= di[d]
#                         newj+= dj[d]
#         N+=1
#
# T = 1
# for tc in range(1,T+1):
#     N = int(input())
#     mtx = [list(map(int,input().split())) for _ in range(100)]
#     for i in range(100):
#         if mtx[0][i] == 1:
#             row, col = 0,i
#             print(ladder(row,col,0))

#
# def ladder(row,col,N):
#     visited=[]
#     stack = [[row,col]]
#
#     di = [0,0,1]
#     dj = [-1,1,0]
#
#     while N!=100:
#         print(stack)
#         nrow,ncol = stack.pop()
#         if mtx[nrow][ncol] == 2:
#             return col
#         else:
#             print('visited: {}'.format(visited))
#             if [nrow,ncol] not in visited:
#                 print('v: {}'.format([nrow, ncol]))
#                 visited.append([nrow,ncol])
#                 for d in range(3):
#                     newi = nrow + di[d]
#                     newj = ncol + dj[d]
#                     if 0<= newi<10 and 0<= newj<10:
#                         if mtx[newi][newj] == 1:
#                             if [newi,newj] not in visited:
#                                 stack.append([newi,newj])
#                                 newi+= di[d]
#                                 newj+= dj[d]
#                                 print(newi,newj)
#         N+=1
# T = 1
# for tc in range(1,T+1):
#     N = int(input())
#     mtx = [list(map(int,input().split())) for _ in range(10)]
#     for i in range(10):
#         if mtx[0][i] == 1:
#             row, col = 0,i
#     print(ladder(row,col,0))

def ladder(row,col):
    global ans
    visited[row][col] = 1

    di = [0,0,1]
    dj = [-1,1,0]

    for d in range(3):
        newi = row+ di[d]
        newj = col+ dj[d]

        if 0<=newi<10 and 0<=newj<10:
            if mtx[newi][newj] == 2:
                ans = 1
                return ans
            if mtx[newi][newj] == 1:
                if visited[newi][newj] == 0:
                    visited[newi][newj] = 1

T = 1
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(10)]
    ans = 0
    for i in range(10):
        if mtx[0][i] == 1:
            visited = [[0]*10 for _ in range(10)]
            print(ladder(0,i))
        if ans == 1:
            print(i)
            break