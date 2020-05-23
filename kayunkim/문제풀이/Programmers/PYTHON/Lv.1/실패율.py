def solution(N, stages):
    answer = []
    bin = {}
    for i in stages:
        if i not in bin:
            bin[i] = 1
        else:
            bin[i]+=1
    new_stage = sorted(bin.items())
    user = len(stages)
    bin2 = {}
    for j in new_stage:
        if j[0] == N+1:
            bin2[j[0]-1]=0/user
        else:
            bin2[j[0]] = j[1]/user
        user-=j[1]
    # print(sorted(bin2.items()))
    ans = sorted(bin2.items(), key=lambda x:x[1], reverse=True)
    for i in ans:
        answer.append(i[0])
    while len(answer) != N:
        if len(answer) not in answer:
            answer.append(len(answer))
        else:
            answer.append(len(answer)+1)
    return answer