T = 10
for tc in range(1,T+1):
    N, pwd = list(input().split())
    ans = list(pwd)
    h = 0
    while h != int(N):
        for i in range(len(pwd)-1):
            if pwd[i] == pwd[i+1]:
                ans.pop(i)
                ans.pop(i)
                break
        else:
            break
        h += 1
        pwd = ans
    print('#{} {}'.format(tc,''.join(ans)))



# T = 10
# for tc in range(1,T+1):
#     N, pwd = list(input().split())
#     ans = list(pwd)
#     for i in range(int(N)-2,-1,-1):
#         if ans[i] == ans[i+1]:
#             ans.pop(i)
#             ans.pop(i)
#             ans.append('')
#     print('#{} {}'.format(tc,''.join(ans)))

T = 2
for tc in range(1,T+1):
    N, pwd = list(input().split())
    ans = list(pwd)