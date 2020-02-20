#피연산자인지 확인 (숫자인지)
def is_number(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False

def isp(token)  #isp: 스택의 top연산자 우선순위
    if toke == '*' or token == '/':
        return 2
    elif token == '+' or token == '-':
        return 1
    elif token == '(':
        return 0

def icp(token)  #icp : 스택으로 들어갈 연산자 우선순위
    if token == '*' or token=='/':
        return 2
    elif token == '+' or token== '-':
        return 1
    elif token =='(':
        return 0

T = 10
operator = ['*','/','-','+']    #연산자
bracket = ['(',')']             #괄호

for tc in range(1,T+1):
    N = int(input())
    infix = list(input())       #중위표기법
    postfix = []                #후위표기법
    stack = []                  #변환을 위한 스택

    #중위 -> 후위
    for c in infix :
        if is_number(c):        #피연산자면 그냥 출력
            postfix.append(c)
        elif c == ')':
            while len(stack) >0:
                top = stack.pop()
                if top == '(':
                    break
                postfix.append(top)
        else:                   #닫는 괄호를 제외한 연산자
            if len(stack) == 0: #스택이 비어있다면
                stack.append(c) #토큰을 스택에 push
            else:               #스택이 비어있지 않으면, 우선순위 비교 icp>isp일 때 push 아니면, pop
                while len(stack) >0:
                    top = stack[-1]
                    if icp(c) > isp(top):
                        stack.append(c)
                        break
                    postfix.append(stack.pop())


    #후위 표기법 -> 스택을 이용해서 계산
    stack = []
    for c in postfix:
        if c not in operator:       #피연산자라면 스택에 넣기
            stack.append(int(c))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if c == '+':
                stack.append(op2+op1)
            elif c == '*':
                stack.append(op2*op1)
            elif c == '-':
                stack.append(op2-op1)
            elif c == '/':
                stack.append(op2/op1)
    result = stack.pop()
    print('#{} {}'.format(tc,result))

