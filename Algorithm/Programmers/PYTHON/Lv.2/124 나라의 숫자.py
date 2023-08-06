def solution(n):
    answer = []
    while n != 0:
        if n%3 == 0:
            answer.append(4)
            n = n//3-1
        elif n%3 == 1:
            answer.append(1)
            n = n//3
        elif n%3 == 2:
            answer.append(2)
            n = n//3
    ans = list(reversed(answer))
    return ''.join(map(str,ans))