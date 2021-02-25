def solution(n):
    num = [1, 2, 3]
    if n <= 3:
        return n
    else:
        for i in range(4, n + 1):
            num[i % 3 - 1] = num[i % 3] + num[i % 3 - 2]
        return num[i % 3 - 1] % 1000000007


def solution(n):
    left, right = 1,2
    if n <= 3:
        return n
    else:
        for i in range(n-2):
            left,right = right, left+right
        return right%1000000007