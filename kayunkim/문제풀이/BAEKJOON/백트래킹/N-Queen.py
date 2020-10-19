def find(cur):
    global cnt, N
    print(cur,sumV)
    if cur == N:
        cnt+=1
        print()
        return
    else:
        for i in range(N):  #가로탐색
            d1_idx = N-1-(cur-i)
            d2_idx = cur+i
            print('mid',cur,i, d1_idx, d2_idx)
            if not v[i] and not diag1[d1_idx] and not diag2[d2_idx]:
                v[i] = 1
                diag1[d1_idx]=1
                diag2[d2_idx]=1
                sumV.append((cur,i))
                find(cur+1)
                v[i] = 0
                diag1[d1_idx] = 0
                diag2[d2_idx] = 0
                sumV.pop()

N = int(input())
cnt = 0
v = [0]*N  #가로
sumV = []
diag1 = [0]*(2*N-1)  #왼쪽대각선
diag2 = [0]*(2*N-1)  #오른쪽대각선
find(0)
print(cnt)