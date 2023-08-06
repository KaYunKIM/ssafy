from itertools import combinations

def solution(nums):
    answer = 0
    combis = list(combinations(nums,3))
    
    for com in combis:
        sumV = sum(com)
        for i in range(2,sumV):
            if sumV%i ==0:
                break
        else:
            answer+=1

    return answer