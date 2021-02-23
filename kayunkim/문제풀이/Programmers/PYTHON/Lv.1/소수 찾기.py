## 시간초과
def solution(n):
    answer = 1
    for i in range(3,n+1):
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            answer+=1
    return answer


def solution(n):
    nums = set([i for i in range(3,n+1,2)])
    for i in range(3,n+1,2):
        if i in nums:
            nums-=set([j for j in range(i*2,n+1,i)])
    return len(nums)+1