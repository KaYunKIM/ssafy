def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n

    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for i in times:
            cnt += mid//i
            if cnt >= n:
                break
        if cnt >= n:   # n명 전체 심사 가능
            answer = mid
            right = mid-1
        else:          # n명 전체 심사 가능하지 않은 경우
            left = mid+1
    return answer