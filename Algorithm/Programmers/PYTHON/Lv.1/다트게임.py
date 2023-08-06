import re

def solution(dartResult):
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    score = p.findall(dartResult)
    bin = []
    for i in score:
        first = int(i[0])
        if i[1] == 'S':
            second = first**1
        elif i[1] == 'D':
            second = first**2
        elif i[1] == 'T':
            second = first**3
        if i[2] == '*':
            if bin:
                bin[-1]*=2
                bin.append(second*2)
                # bin.append(bin[-1]+second*2) 시간초과(?)
            else:
                bin.append(second*2)
        elif i[2]== '#':
            bin.append(second*(-1))
        elif i[2]== '':
            bin.append(second)
    return sum(bin)