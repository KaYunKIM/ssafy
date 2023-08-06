# import math
# def solution(n):
#     if math.sqrt(n).is_integer():
#         return (math.sqrt(n)+1)**2
#     else:
#         return -1
#     return answer

def solution(n):
 ans = n**(1/2)
    if ans.is_integer():
        return (ans+1)**2
    else:
        return -1