def solution(n, computers):
    N = len(computers)
    v = [0]*(N)
    def find(cur,sumV,N):
        if cur == N:
            sumV+=1
            return sumV
        else:
            v[cur]=1
            for i in range(N):
                if computers[cur][i] == 1 and v[i]==0:
                    find(cur+1,sumV,N)
                elif computers[cur][i] == 0:
                    sumV+=1
                    return sumV
    a = find(0,0,n)
    a+= v.count(0)
    return a


# def find(cur, k, num, computers):
#     if cur == k:
#
#     else:
#         for i in num:
#             if not v[i] and computers[cur][i] == 1:
#                 v[i] = 1
#                 find(cur + 1, k, num, computers)
#                 v[i] = 0
#
#
# def solution(n, computers):
#     visited = [0] * n
#
#     for c in computers:
#         find(0, n-1, c, computers)
#
#     return answer





# tc2
# di = [1, 1]
# dj = [0, 1]
#
#
# def solution(n, computers):
#     cnt = 1
#     i, j = 0, 0
#     while i != (n - 1) and j != (n - 1):
#         for d in range(2):
#             newi = i + di[d]
#             newj = j + dj[d]
#             if 0 <= newi < n and 0 <= newj < n:
#                 if computers[newi][newj] == 0:
#                     cnt += 1
#                 print(newi, newj)
#         i, j = newi, newj
#     return cnt