def solution(n):
    answer = 0
    v = [0] * n
    dx = [0] * (2 * n - 1)
    dy = [0] * (2 * n - 1)

    def find(cur):
        nonlocal answer

        if cur == n:
            answer += 1
            return

        for i in range(n):
            if not v[i] and not dx[cur + i] and not dy[cur - i]:
                v[i], dx[cur + i], dy[cur - i] = 1, 1, 1
                find(cur + 1)
                v[i], dx[cur + i], dy[cur - i] = 0, 0, 0

    find(0)
    return answer