def solution(n):
    answer = []

    def hanoi(n, From, Mid, To):
        if n == 0:
            return
        hanoi(n - 1, From, To, Mid)
        answer.append([From, To])
        hanoi(n - 1, Mid, From, To)

    hanoi(n, 1, 2, 3)
    return answer