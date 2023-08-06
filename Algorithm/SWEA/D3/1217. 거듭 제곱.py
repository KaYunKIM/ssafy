def square(M):
    if M == 1:
        return N
    else:
        return square(M-1)*N

T = 10
for tc in range(1,T+1):
    T = int(input())
    N,M = list(map(int,input().split()))
    print('#{} {}'.format(tc,square(M)))

#
# def fibo(n):
#     if n ==1 or n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# print(fibo(10))

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return sum(n-1)+n
#
# print(sum(4))