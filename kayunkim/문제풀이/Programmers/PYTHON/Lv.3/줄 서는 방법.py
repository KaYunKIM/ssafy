from itertools import permutations


def solution(n, k):
    line = [i for i in range(1, n + 1)]
    answer = list(permutations(line))
    # print(answer[k-1])

    return answer[k - 1]