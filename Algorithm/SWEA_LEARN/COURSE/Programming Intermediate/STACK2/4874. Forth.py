def forth():
    stack = []
    for i in lst:
        if i == '+' or i == '-' or i == '*' or i == '/':
            if len(stack)>= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(a//b)
            else:
                return 'error'
        elif i == '.':
            if len(stack)== 1:
                return stack.pop()
            else:
                return 'error'
        else:
             stack.append(i)

T = int(input())
for tc in range(1,T+1):
    lst= list(input().split())
    print('#{} {}'.format(tc,forth()))