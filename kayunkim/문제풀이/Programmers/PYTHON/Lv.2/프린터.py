def solution(priorities, location):
    answer = 0
    bin = []
    for idx, val in enumerate(priorities):
        bin.append((idx,val))
    while bin:
        idx,val = bin.pop(0)
        if max(priorities) > val:
            bin.append((idx,val))
        else:
            answer+=1
            priorities.remove(val)
            if idx == location:
                break
    return answer