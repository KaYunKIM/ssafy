from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for j in orders:
            temp+=combinations(sorted(j),i)
        cnt = Counter(temp)
        if cnt:
            maxV = max(cnt.values())
            if maxV >=2:
                for k,v in cnt.items():
                    if v == maxV:
                        # print(k)
                        answer.append(''.join(k))
    return sorted(answer)