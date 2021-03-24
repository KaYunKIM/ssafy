def solution(N, number):
    answer = 10000000

    def find(cur, sumV):
        nonlocal answer, N, number
        if sumV > answer:
            return

        if cur == number:
            if sumV < answer:
                answer = sumV
            return

        find(cur + N, sumV + 1)
        find(cur - N, sumV + 1)
        find(cur * N, sumV + 1)
        find(cur // N, sumV + 1)

    for i in range(1, len(str(number)) + 1):
        num = int(str(N) * i)
        find(num, 1)

    if answer < 8:
        return answer
    else:
        return -1