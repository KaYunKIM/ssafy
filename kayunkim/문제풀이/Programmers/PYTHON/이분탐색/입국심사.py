def solution(n, times):
    answer = 0
    left = 1
    right = min(times)*n

    while left < right:
        middle = (left + right) // 2
        temp = n
        for i in times:
            temp-= mid//i
            if temp <= 0:
                answer = mid
                right = mid-1
                break
        else:
            left = middle + 1
    return answer