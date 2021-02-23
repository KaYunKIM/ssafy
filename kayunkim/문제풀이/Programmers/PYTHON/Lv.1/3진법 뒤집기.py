def solution(n):
    tri = ''
    while n != 0:
        tri+= str(n%3)
        n = n//3
        
    return int(tri,3)