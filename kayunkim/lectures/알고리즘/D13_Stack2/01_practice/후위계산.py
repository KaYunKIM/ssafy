'''
6528-*2/+
-9.0

1. 피연산자를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산, 연산결과를 스택에 push
3. 수식이 끝나면 마지막으로 스택을 pop해서 출력

'''

# postfix = list(input())
# stack = []
# isp = {'(': 0, '+':1, '-':1, '*':2, '/':2, ')':0}
# icp = {'(': 3, '+':1, '-':1, '*':2, '/':2, ')':0}
#
# for c in postfix:
#     if c not in isp.keys():
#         stack.append(c)
#     else:
#         if icp[c] > isp[c]:
#             stack.append(c)
#         else:
#             stack.pop()
#     print(stack.pop())


postfix = list(input())
stack = []
operator = ['+','-','*','/']

for c in postfix:
    if c not in operator:
        stack.append(int(c))
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        if c == '+':
            stack.append(op2+op1)
        if c == '-':
            stack.append(op2-op1)
        if c == '*':
            stack.append(op2*op1)
        if c == '/':
            stack.append(op2/op1)
print(stack.pop())