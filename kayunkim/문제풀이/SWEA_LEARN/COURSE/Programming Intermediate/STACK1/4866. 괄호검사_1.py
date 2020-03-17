def gh(lst):
    stack = []
    for i in lst:
        if i in '({':
            stack.append(i)
        elif i in ')}':
            if not stack:
                return 0
            else:
                r = stack.pop()
                if i == ')':
                    if r == '{':
                        return 0
                if i == '}':
                    if r == '(':
                        return 0

    if len(stack) == 0:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    lst = input()
    print(gh(lst))