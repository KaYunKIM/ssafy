def queen(Q):
    global cnt, N
    if Q == N+1:
        cnt+=1
        return
    else:
        for j in range(1,N+1):
            if v[j]==0 and diag1[Q+j-1]==0 and diag2[N-Q+j-2]==0:
                v[j]=1
                diag1[Q+j-1]=1
                diag2[N-Q+j-2]=1
                queen(Q+1)
                v[j]=0
                diag1[Q+j-1]=0
                diag2[N-Q+j-2]=0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    diag1 = [0]*(2*N)  #(i+j-1)
    diag2 = [0]*(2*N)  #(N-i+j-2)
    cnt = 0
    v = [0]*(N+1)
    queen(1)
    print('#{} {}'.format(tc,cnt))


# def queen(i,j):
#     visited = [[0] * N for _ in range(N)]
#     visited[i][j] = 1
#     cnt = 0
#     while True:
#         if i == N-1:
#             cnt+=1
#             return
#         else:
#             for col in range(i+1,N):
#                 visited[col][j] = 1
#
#             for dr in range(N):
#                 if 0<= dr<N:
#                     visited[dr][dr] = 1
#
#             for dl in range(N):
#                 if 0 <= dl < N:
#                     visited[dl][N-dl-1] = 1
#
#             print(visited,i)
#             for newj in range(N):
#                 if visited[i+1][newj] == 0:
#                     queen(i+1, newj)
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     for k in range(N):
#         print(queen(0,k))
#
#     # print('#{} {}'.format(tc,cnt))