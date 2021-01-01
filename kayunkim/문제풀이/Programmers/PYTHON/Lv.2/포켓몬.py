def solution(nums):
    temp = []
    for i in range(len(nums)):
        if nums[i] not in temp:
            temp.append(nums[i])
        if len(temp) == len(nums)/2:
            break
    return len(temp)


##시간 단축
def solution(nums):
    answer = 0
    for i in set(nums):
        if answer < len(nums)//2:
            answer+=1
    return answer
