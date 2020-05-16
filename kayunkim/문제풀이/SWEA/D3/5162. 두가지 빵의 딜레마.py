def bread(price):
    global C, N
    cnt=0
    while price <= C:
        price+=N
        cnt+=1
    return cnt

T = int(input())
for tc in range(1,T+1):
    A,B,C = list(map(int,input().split()))
    N = min(A,B)
    print('#{} {}'.format(tc,bread(min(A,B))))