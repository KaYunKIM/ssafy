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
    print(cnt)