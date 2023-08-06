def equal(N,M):
    for i in range(len(M)-len(N)+1):
        if M[i:i+len(N)] == N:
            ans = 1
            break
        else:
            ans = 0
    return ans

T = int(input())
for tc in range(1,T+1):
    N = input()
    M = input()
    print('#{} {}'.format(tc,equal(N,M)))