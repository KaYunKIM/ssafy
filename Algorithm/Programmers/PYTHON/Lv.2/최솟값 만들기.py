def solution(A,B):
    minV = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        minV+=A[i]*B[i]
    return minV