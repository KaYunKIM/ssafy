거듭제곱 : 반복문
def power(base,exponent):
    if base == 0:
        return 1
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(power(10,2))


#분할정복
'''
c^8 = c^4 * c^4
c^9 = c^4 * c^4 * c
'''

def power2(base,exponent):
    if exponent == 0 or base == 0:
        return 1
    if exponent%2 == 0:     #짝수이면
        newbase = power2(base,exponent/2)
        return newbase*newbase
    else:                   #홀수이면
        newbase = power2(base,(exponent-1)/2)
        return newbase*newbase*base
print(power2(2,10))