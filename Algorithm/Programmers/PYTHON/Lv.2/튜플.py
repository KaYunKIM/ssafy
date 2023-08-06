def solution(s):
    answer = []
    temp = {}
    num = ''
    for i in s:
        if i.isnumeric():
            num+=i
        else:
            if num:
                if num not in temp:
                    temp[num] = 1
                else:
                    temp[num]+=1
                num = ''
    result = sorted(temp.items(), key=lambda x:x[1], reverse=True)
    answer = [int(i[0]) for i in result]
    return answer


## 시간 단축
from collections import Counter

def solution(s):
    s = s.replace("{", "").replace("}","")
    temp = Counter(s.split(','))
    newtemp = sorted(temp.items(), key=lambda x:x[1], reverse=True)
    answer = [int(i[0]) for i in newtemp]
    return answer