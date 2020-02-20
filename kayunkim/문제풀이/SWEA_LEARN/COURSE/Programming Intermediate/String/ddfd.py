"n = int(input())

stan = n**0.5

a = round(stan)
b = (n + a)/2

while str(a)[:5] != str(b)[:5]:
    if a**2 < n < b**2:
        c = (b+a)/2
        if c**2 > n:
            b = c
        else:
            a = c

print(str(a)[:5])"