import math

def solution(progresses, speeds):
    answer = []
    temp = []
    cnt = 1
    for x in range(len(progresses)):
        days = math.ceil((100-progresses[x])/speeds[x])
        if not temp or temp[0]>= days:
            temp.append(days)
        else:
            answer.append(len(temp))
            temp = [days]
    answer.append(len(temp))

    return answer