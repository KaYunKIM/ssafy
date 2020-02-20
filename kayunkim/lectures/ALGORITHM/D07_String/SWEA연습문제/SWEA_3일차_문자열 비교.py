# T = int(input())
# for tc in range(1,T+1):
#     N = str(input())
#     M = str(input())
#
#     cnt = 0
#     for i in range(len(M)):
#         if M[i] in N:
#             cnt +=
#
#     ans = '0'
#     if len(N) <= cnt:
#         if N in M:
#             ans = '1'
#
#     print('#{} {}'.format(tc,ans))

def kayun(N,M):
    for i in range(len(M)+1-len(N)):
        if M[i:len(N)+i] == N:
            result = '1'
            break
        else:
            result = '0'
    return result

T = int(input())
for tc in range(1,T+1):
    N = input()
    M = input()

    print(kayun(N,M))

