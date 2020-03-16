import sys
sys.stdin = open('C:\\Users\\multicampus\\Desktop\\kayunkim\\lectures\\알고리즘\\D10_Stack\\input.txt', 'r')


def find_match():
    s = list()
    for i in range(len(txt)):
        if txt[i] == '(':        #문자가 여는 괄호면
            s.append(txt[i])
        elif txt[i] == ')':     #문자가 닫는 괄호면
            if(len(s) == 0):
                return 0
            else:
                s.pop()         #스택에서 하나 빼서 버리기
    #모든 반복 완료 후
    if len(s) != 0:             #스택에 괄호가 남았다면
        return 0
    else:
        return 1


T = int(input())
for tc in range(1,T+1):
    txt = input()
    print('#{} {}'.format(tc,find_match()))