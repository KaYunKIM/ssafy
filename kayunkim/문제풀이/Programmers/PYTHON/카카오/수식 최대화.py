def solution(expression):
    answer = 0

    tools = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '+', '-'],
        ['*', '-', '+']
    ]

    def find(tool, cur, exp):
        if cur == 2:  # 숫자+(기호)+숫자
            return str(eval(exp))

        if tool[cur] == '+':
            ans = eval('+'.join([find(tool, cur + 1, i) for i in exp.split('+')]))

        if tool[cur] == '-':
            ans = eval('-'.join([find(tool, cur + 1, i) for i in exp.split('-')]))

        if tool[cur] == '*':
            ans = eval('*'.join([find(tool, cur + 1, i) for i in exp.split('*')]))

        return str(ans)

    for tool in tools:
        res = abs(int(find(tool, 0, expression)))
        answer = max(answer, res)

    return answer