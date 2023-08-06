T = int(input())
for tc in range(1,T+1):
    lst = input()
    bin = {'(':')', '{':'}'}
    stack = []
    ans = 1
    for i in lst:
        if i in '({':
            stack.append(i)
        elif i in ')}':
            if len(stack)==0:
                ans = 0
                break
            else:
                if bin[stack[-1]] == i:
                    stack.pop()
                else:
                    ans = 0
    if len(stack) !=0:
        ans = 0
    print('#{} {}'.format(tc,ans))