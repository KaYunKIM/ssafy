import copy
def solution(number, k):
    number = list(number)
    cur = 1
    ans_len = copy.deepcopy(len(number))
    while len(number)!= ans_len-k and cur!= len(number):
        if int(number[cur-1]) < int(number[cur]):
            h = cur
            while h!=0 and int(number[h-1]) < int(number[h]) and len(number)> ans_len-k:
                # print(h,int(number[h-1]),int(number[h]))
                number.del(number[h-1])
                # number = number[0:h-1] + number[h:]
                cur-=1
                h-=1
        cur+=1
        # print(number)
    if len(number) == ans_len:
        return ''.join(number[:len(number)-k])
    return ''.join(number)

print(solution("4177252841", 4))
print(solution("999999", 2))
