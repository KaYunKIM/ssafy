# T = 10
# for tc in range(1,T+1):
#     N, pwd = list(input().split())
#     ans = list(pwd)
#     h = 0
#     while h != int(N):
#         for i in range(len(pwd)-1):
#             if pwd[i] == pwd[i+1]:
#                 ans.pop(i)
#                 ans.pop(i)
#                 break
#         else:
#             break
#         h += 1
#         pwd = ans
#     print('#{} {}'.format(tc,''.join(ans)))

# a = list(input().split())
# a = a[1]
# a = list(a)
#
# for i in range(len(a) - 2, -1, -1):
#     if a[i] == a[i + 1]:
#         a.pop(i)
#         a.pop(i)
#         a.append('')
#
# print('#{} {}'.format(test_number + 1, ''.join(a)))



T = 2
for tc in range(1,T+1):
    N, pwd = list(input().split())
    ans = list(pwd)

    for i in range(N-2,-1,-1):
        if ans[i] == ans[i+1]:
            ans.pop(i)
            ans.pop(i)
            print(ans)