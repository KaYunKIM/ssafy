def find(P,Palpabet):
    l = 1
    r = P
    c = (l + r) // 2
    cnt = 1
    while c != Palpabet:
        if c > Palpabet:
            r = c
            c = (l + r) // 2
        elif c < Palpabet:
            l = c
            c = (l + r) // 2
        cnt += 1
    return cnt

T = int(input())
for tc in range(1,T+1):
    P,Pa,Pb = list(map(int,input().split()))

    A = find(P,Pa)
    B = find(P,Pb)

    if A < B:
        ans = 'A'
    elif A > B:
        ans = 'B'
    else:
        ans = '0'
    print('#{} {}'.format(tc,ans))