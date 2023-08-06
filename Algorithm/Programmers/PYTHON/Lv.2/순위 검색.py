## 효율성 실패
def solution(info, query):
    answer = [0]*len(query)
    for q in range(len(query)):
        reform  = query[q].replace('and ', '').replace('- ', '').split(' ')
        for i in info:
            i = i.split(' ')
            if len(reform)>1:
                if set(reform[:-1]+i[:-1]) == set(i[:-1]):
                    if int(i[-1]) >= int(reform[-1]): 
                        answer[q]+=1
            else:
                if int(i[-1]) >= int(reform[0]):
                    answer[q]+=1
                
    return answer