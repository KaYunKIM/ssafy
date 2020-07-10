def solution(answers):
    answer = []
    a= [1,2,3,4,5]
    b= [2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    cnta = 0
    cntb = 0
    cntc = 0
    for idx,val in enumerate(answers):
        if a[idx%5] == val:
            cnta+=1
        if b[idx%8] == val:
            cntb+=1
        if c[idx%10] == val:
            cntc+=1
    ans = [(cnta,1), (cntb,2), (cntc,3)]
    for i in ans:
        if i[0] == max(ans)[0]:
            answer.append(i[1])
    return answer