from itertools import permutations


def solution(n, k):
    line = [i for i in range(1, n + 1)]
    answer = list(permutations(line))
    # print(answer[k-1])

    return answer[k - 1]


import math

def solution(n, k):
    answer = []
    num = [i for i in range(1, n+1)]

    while n != 0:
        temp = math.factorial(n)//n 
        index = k/temp
        k%=temp

        if k == 0:
            answer.append(num.pop(index-1))
        else:
            answer.append(num.pop(index))
        n -= 1

    return answer