def solution(x, n):
    answer = []
    i = x
    while len(answer)!= n:
        answer.append(i)
        i+=x
    return answer