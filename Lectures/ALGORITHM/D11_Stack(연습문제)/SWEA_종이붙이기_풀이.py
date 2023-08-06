def f(n):
    if n ==0 or n == 1:
        return 1
    return f(n-1) + 2*f(n-2)


T = int(input())
for tc in range(1,T+1):
    N=int(input())//10
    print('#{} {}'.format(tc,f(N)))

