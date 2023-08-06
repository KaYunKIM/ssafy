# T = int(input())
# for tc in range(1,T+1):
#     lst = list(input())
#     bin = []
#     ans = 1
#     for i in range(len(lst)):
#         if lst[i] == '{':
#             bin.append(lst[i])
#         elif lst[i] == '}':
#             if len(bin) == 0 or bin[-1] == '(':
#                 ans = 0
#                 break
#             elif '{' == bin[-1]:
#                 bin.pop()
#         elif lst[i] == '(':
#             bin.append(lst[i])
#         elif lst[i] == ')':
#             if len(bin) == 0 or bin[-1] == '{':
#                 ans = 0
#                 break
#             elif '(' == bin[-1]:
#                 bin.pop()
#     if ans == 0:
#         print('#{} 0'.format(tc))
#     else:
#         if len(bin) == 0:
#             print('#{} 1'.format(tc))
#         else:
#             print('#{} 0'.format(tc))

T = int(input())
diction = {'(':')', '{':'}'}
for tc in range(1,T+1):
    lst = input()
    bin = []
    result = 1
    for i in lst:
        if i in '({':
            bin.append(i)
        elif i in ')}':
            if len(bin) == 0:
                result = 0
                break
            else:
                if diction[bin.pop()] != i:
                    result = 0
    if len(bin) != 0:
        result = 0
    print('#{} {}'.format(tc, result))



# bric = {'[':']', '{':'}', '(':')'}
# for T in range(int(input())):
#     stack = []
#     sent = input()
#     result = 1
#     for i in sent:
#         if i in '[{(':
#             stack.append(i)
#         elif i in ')}]':
#             if stack == []:
#                 result = 0
#                 break
#             a = stack.pop()
#             if bric[a] != i:
#                 result = 0
#                 break
#     if stack != []:
#         result = 0
#     print('#{} {}'.format(T + 1, result))

