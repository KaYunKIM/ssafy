def find(cur_i, cur_j, sumv):
    global cnt, N
    print(cur_i, cur_j, sumv, sumV)
    if sumv == N-1:
        cnt+=1
        print()
        return
    else:
        for i in range(cur_i+1, N):  # 깊이탐색
            for j in range(N):
                d1_idx = N-1-(i-j)
                d2_idx = i+j
                # print('mid',i,j, d1_idx, d2_idx)
                if not v[j] and not diag1[d1_idx] and not diag2[d2_idx]:
                    v[j] = 1
                    diag1[d1_idx]=1
                    diag2[d2_idx]=1
                    sumV.append((i,j))
                    find(i,j, sumv+1)
                    v[j] = 0
                    diag1[d1_idx] = 0
                    diag2[d2_idx] = 0
                    sumV.pop()

N = int(input())
cnt = 0
v = [0]*N
sumV = []
diag1 = [0]*(2*N-1)
diag2 = [0]*(2*N-1)
for i in range(N):
    v[i] = 1
    diag1[N-1+i] = 1
    diag2[i] = 1
    sumV.append((0,i))
    find(0, i, 0)
print(cnt)