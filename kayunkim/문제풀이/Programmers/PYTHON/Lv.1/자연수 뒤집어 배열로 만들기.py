def solution(n):
    n = str(n)
    return list(int(i) for i in n[::-1])

    # return [int(i) for i in str(n)[::-1]]