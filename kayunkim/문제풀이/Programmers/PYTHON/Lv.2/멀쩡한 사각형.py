import math

def solution(w,h):
    square = w*h
    cut = w+h-math.gcd(w,h)
    return square - cut