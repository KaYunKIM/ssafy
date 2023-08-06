def solution(n,a,b):
    answer = 1
    while True:
        if a%2 == 1:
            a+=1
        a = a//2

        if b%2 == 1:
            b+=1
        b = b//2
        
        if a == b:
            return answer
        
        answer+=1