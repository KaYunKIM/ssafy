from itertools import combinations, permutations

def solution(numbers):
    answer = []
    combi = []
    
    for i in range(1,len(numbers)+1):
        combi+=combinations(numbers, i)
    combi = set(combi)
    
    newtemp = []
    for com in combi:
        temp = []
        com = ''.join(com)
        temp+=permutations(com, len(com))
        for i in temp:
            newtemp.append(int(str(i).replace('(', '').replace(')','').replace("'",'').replace(',','').replace(' ','')))

    newtemp = set(newtemp)
    for num in newtemp:
        if num >1:
            for j in range(2,num):
                if num%j == 0:
                    break
            else:
                answer.append(num)
                
    return len(answer)