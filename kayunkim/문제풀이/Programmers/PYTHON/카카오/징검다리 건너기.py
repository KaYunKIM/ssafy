## 실패
def solution(stones, k):
    answer = 0

    temp = 0
    while temp < k:
        for i in range(len(stones)):
            if stones[i]:
                stones[i] -= 1
            else:
                temp += 1
            if temp == k:
                break

        answer += 1
        if sum(stones) == 0:
            return answer

    return answer


def solution(stones, k):
    answer = 0

    def find(mid):
        cnt = 0
        for i in stones:
            if i < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                return False
        return True

    left = 1
    right = max(stones) + 1
    while right - left != 1:
        mid = (left + right) // 2
        if find(mid):
            left = mid
        else:
            right = mid

    return left

