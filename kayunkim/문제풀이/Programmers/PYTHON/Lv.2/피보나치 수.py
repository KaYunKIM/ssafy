def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2)) % 1234567


def solution(n):
    answer = fibo(n)
    return answer