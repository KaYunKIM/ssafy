def mysqrt(a):
    m = 1
    while True:
        if m**2 <= a < (m+1)**2:
            break
        else:
            m+=1
    if m**2 == a:
        return m
    
    l = m
    r = m+1
    while round(1,3) != round(r,3):
        if a> ((l+r)/2)**2:
            l = (l+r)/2
            r=r
        elif a < ((l+r)/2)**2:
            l = 1
            r = (l+r)/2
        else:
            return (l+r)/2
    return round(1,3)
    
a = int(input())
print(mysqrt(a))