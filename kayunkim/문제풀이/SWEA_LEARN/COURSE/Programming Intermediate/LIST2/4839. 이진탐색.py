T = int(input())
for tc in range(1,T+1):
    P,Pa,Pb = list(map(int,input().split()))
    l =1
    r = P
    c = (l+r)//2
    cnta= 1
    while c != Pa:
        if c> Pa:
            r = c
            c = (l + r) // 2
        elif c < Pa:
            l = c
            c = (l + r) // 2
        cnta+= 1
        print(l, r, c)
    print(cnta)

    l = 1
    r = P
    c = (l + r) // 2
    cntb = 1
    while c != Pb:
        if c> Pb:
            r = c
            c = (l + r) // 2
        elif c < Pb:
            l = c
            c = (l + r) // 2
        cntb+= 1
        print(l, r, c)
    print(cntb)

    if cnta < cntb:
        ans = 'A'
    elif cnta > cntb:
        ans = 'B'
    else:
        ans = '0'
    print('#{} {}'.format(tc,ans))