import heapq

def solution(d, budget):
    cnt = 0
    heapq.heapify(d)
    while d:
        if  budget - d[0] >=0:
            budget-= heapq.heappop(d)
            cnt+=1
        else:
            return cnt
    return cnt
