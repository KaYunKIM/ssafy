T = int(input())
for tc in range(1,T+1):
    L,U,X = list(map(int,input().split()))
    ans = 0
    if X< L:
        ans = L-X
    elif X > U:
        ans = -1
    print('#{} {}'.format(tc,ans))

# T = int(input())
# for tc in range(1,T+1):
#     L,U,X = list(map(int,input().split()))
#     if X< L:
#         ans = L-X
#     elif X > U:
#         ans = -1
#     elif L<X<U:
#         ans = 0
#     print('#{} {}'.format(tc,ans))