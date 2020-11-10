def solution(m, n, puddles):
    jido = [[1]*(m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i != 0 and j != 0:
                jido[i][j] = jido[i-1][j]+jido[i][j-1]
            if [i+1,j+1] in puddles:
                jido[i][j]=0
    return jido[-1][-1]