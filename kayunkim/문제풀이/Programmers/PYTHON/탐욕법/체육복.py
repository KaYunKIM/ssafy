def solution(n, lost, reserve):
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for j in reserve:
        if j-1 in lost:
            lost.remove(j-1)
            reserve.remove(j)
        elif j+1 in lost:
            lost.remove(j+1)
            reserve.remove(j)
    return n-len(lost)