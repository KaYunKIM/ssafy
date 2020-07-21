import copy
def solution(number, k):
    number = list(number)
    cur = 1
    ans_len = copy.deepcopy(len(number))-k
    while len(number)!= ans_len:
        if int(number[cur-1]) < int(number[cur]):
            h = cur
            while h!=0 and int(number[h-1]) < int(number[h]) and len(number)> ans_len:
                print(h,int(number[h-1]),int(number[h]))
                number.remove(number[h-1])
                cur-=1
                h-=1
        cur+=1
        print(number)
    return ''.join(number)

print(solution("4177252841", 4))
