def solution(participant, completion):
    ans = 0
    participant.sort()
    completion.sort()
    for i in range(len(completion)-1,-1,-1):
        if participant[i] != completion[i]:
             ans = participant[i]
        elif ans ==0:
            ans = participant[-1]
    return ans

#라이브러리 사용
from collections import Counter

def solution(participant, completion):
    cnt = Counter(participant)- Counter(completion)
    # return list(cnt)[0]
    for ans in cnt:
        return ans


## 시간초과
def solution(participant, completion):
    ans = ''
    for p in participant:
        if p not in completion:
            ans+=p
        elif participant.count(p)-completion.count(p)!=0:
            ans+=p
            break
    return ans


## 시간초과
def solution(participant, completion):
    ans = ''
    participant.sort()
    completion.sort()
    for p in participant:
        if participant.count(p)>completion.count(p):
            ans+=p
            break
    return ans