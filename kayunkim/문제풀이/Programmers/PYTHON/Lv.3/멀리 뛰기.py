# 시간초과
def solution(n):
    answer = 0
    def find(sumV):
        nonlocal n, answer
        if sumV == n:
            answer += 1
            return

        for i in range(1, 3):
            if sumV + i <= n:
                find(sumV + i)

    for i in range(1, 3):
        find(i)
    return answer % 1234567


# DP 점화식
def solution(n):
    answer = [0] * (n + 1)
    answer[0] = 1
    answer[1] = 2

    for i in range(n + 1):
        if i >= 2:
            answer[i] = (answer[i - 2] + answer[i - 1]) % 1234567

    return answer[n - 1]