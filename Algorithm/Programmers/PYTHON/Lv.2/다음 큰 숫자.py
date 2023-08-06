def solution(n):
    answer = 0
    i = 1
    while True:
        if bin(n+i).count('1')== bin(n).count('1'):
            return n+i
        i+=1