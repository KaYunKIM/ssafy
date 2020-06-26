def solution(clothes):
    answer = 1
    bin = {}
    for c in clothes:
        if c[1] not in bin:
            bin[c[1]] = [c[0]]
        else:
            bin[c[1]].append(c[0])
    for k,v in bin.items():
        answer*=len(v)+1
    return answer-1