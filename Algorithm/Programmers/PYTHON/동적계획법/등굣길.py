def solution(m, n, puddles):
    jido = [[0]*(m+1) for _ in range(n+1)]
    jido[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            if [j,i] in puddles:
                jido[i][j]=0
            else:
                jido[i][j] = jido[i-1][j]+jido[i][j-1]
    return jido[-1][-1]%1000000007