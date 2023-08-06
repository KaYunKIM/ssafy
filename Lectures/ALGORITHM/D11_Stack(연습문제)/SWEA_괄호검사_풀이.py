def find():
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '{':
            s.append(str[i])
        elif str[i] == ')' or str[i] == '}':
            if not s:       #닫는 괄호일 때 스택이 비어있다면
                return 0
            r = s.pop()
            if (str[i] == '}' and r == '(') or str[i] == ')' and r== '{'):
                return 0    #짝이 아닐 경우
    if len(s) == 0:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1,T+1):
    lst = list(input())

    print('#{} {}'.format(tc, result))

