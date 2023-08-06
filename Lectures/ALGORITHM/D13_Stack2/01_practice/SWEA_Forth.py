def find():
    s = []
    for i in range(len(code)):
        if code[i] == '+' or code[i] == '-' or code[i] == '*' or code[i] == '/':
            if len(s)>=2:       #연산자를 만났을 때 스택에 2개 이상 있는지 확인
                op2 = int(s.pop())
                op1 = int(s.pop())
                if code[i] == '+':      #각 연산자에게 맞게 연산 -> 연산결과 스택에 넣기
                    s.append(op1 + op2)
                elif code[i] == '-':
                    s.append(op1 - op2)
                elif code[i] == '*':
                    s.append(op1 * op2)
                elif code[i] == '/':
                    s.append(op1 // op2)
            else:                       #연산자 만났을 때 스택에 2개 이상 없으면 error
                return 'error'
        elif code[i] != ' ' and code[i] != ',':     #피연산자면
            s.append(code[i])
        elif code[i] = '.':             #마침표 만나면
            if len(s) == 1:             #스택에 있는 연산결과 리턴 -> 단, 피연산자가 하나일때만
                return s.pop()
            else:
                return 'error'


T = int(input())
for tc in range(1,T+1):
    code = list(input().split())
    print('#{} {}'.format(tc, find()))