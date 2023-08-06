def solution(n, words):
    answer = [0,0]
    temp = {}
    for i in range(len(words)):
        answer[0] = i%n+1
        answer[1] = i//n+1
        if words[i] not in temp:
            temp[words[i]] = 1
        else:
            return answer
        if i != 0:
            if words[i][0] != words[i-1][-1]:
                return answer
    return [0,0]
