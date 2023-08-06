import math

def solution(w,h):
    area = w*h
    cut = (w+h)-math.gcd(w,h)
    return area - cut