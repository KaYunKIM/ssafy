def binarysearch(P,page):
    l = 1
    r = P
    c = int((l+r)/2)
    cnt = 1
    while page != c:
        if c < page:
            l = c
            c = int((l + r) / 2)
        else:
            r = c
            c = int((l + r) / 2)
        cnt+= 1
    return cnt

T = int(input())

for tc in range(1,T+1):
    P,Pa,Pb = map(int,input().split())

    A = binarysearch(P,Pa)
    B = binarysearch(P,Pb)

    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'
    elif A == B:
        result = '0'

    print('#{} {}'.format(tc, result))