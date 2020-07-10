def solution(skill, skill_trees):
    answer=0
    for i in skill_trees:
        bin = []
        for j in i:
            if j in skill:
                bin.append(j)
        for k in range(len(bin)):
            if skill[k] != bin[k]:
                break
        else:
            answer+=1
    return answer