def solution(citations):
    answer = 0
    h = 0
    while h!= len(citations):
        y = 0
        n = 0
        for c in citations:
            if citations[h] <= c:
                y+=1
            else:
                n+=1
        if min(y,citations[h])> answer:
            answer = min(y,citations[h])
        h+=1
    return answer