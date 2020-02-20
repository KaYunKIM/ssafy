#재귀함수
#자기자신을 호출하는 함수

'''
재귀 함수의 구조
기본 파트 :  base case
    적어도 하나의 recursion에 빠지지 않는 경우가 존재해야 함
유도 파트 :  recursive case
    recursion을 반복하다보면 결국 base case로 수렴해야 함
'''


# def func(k):
#     if k < 0:           #func()가 호출될 때마다 k값이 줄어듬, k가 0보다 작아지면, 리턴하도록 설정
#         return
#     print('hello')
#     func(k-1)
#
# func(5)

# #재귀함수를 이용해서 1~10까지의 합을 구하세요.
# def sum(k,total):
#     if k <= 0:
#         print(total)
#         return
#     else:
#         sum(k-1, total+k)
# sum(10,0)           #시작지점 -> sum(10,0) -> sum(9,10) -> sum(8,19) -> sum(-1,55)
#
#
# def sum2(k):
#     if k  == 0:
#         return 0
#     else:
#         return k + sum2(k-1)
# print(sum2(5))

# def func1(k):
#     func1(1)
#     sum = 0
#     while k < 11:
#         sum += k
#         k+=1
#     return sum
#
# print(func1())


#정해진 횟수만큼 호출하기
#호출 횟수에 대한 정보를 인자로 전달
#정해진 횟수에 다다르면 재귀호출 중단

# def f(n,k):
#     if n == k:   #재귀 호출 완료 시 해야하는 작업 -> 재귀 호출 종료 부분
#         return
#     else:
#         print(n)    #재귀호출 시 해야하는 작업 -> 재귀 호출 부분
#         f(n+1,k)
#     pass
# f(0,5) #n: 변하는 숫자 k: 지정한 횟수


'''
원하는 조건을 찾으면 중단하는 경우
주어진 집합에 v가 있으면 1, 없으면 0을 리턴하는 재귀함수
'''
# a= [3,7,6,2,1,4,8,5]
# v = 2
# def find(n,k,v):
#     if n == k:
#         return 0
#     if a[n] == v:
#         return 1
#     else:
#         r = find(n+1,k,v)
#         return r
#
# print(find(0,len(a),v))


'''
팩토리알
3! = 3*2*1 = 3*2!
2! = 2*1
1! = 1
0! = 1

f(n) = n* f(n-1)
f(1) = 1
f(0) = 1


'''

# def fac(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*fac(n-1)
#
# print(fac(5))

# mul = 1
# for i in range(1,6):
#     mul *= i
# print(mul)

'''
피보나치 수열
'''
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)    #앞의 수 + 앞의 앞의 수

print(fibo(5))


#메모이제이션 : 연산결과를 저장 -> 중복계산을 안함
#메모를 저장하기 위한 배열을 할당하고 0으로 초기화

def fibo1(n):
    #n이 2보다 같거나 크고 n이 메모 길이보다 길면 -> 아직 계산되지 않았다면
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1)+fibo1(n-2))      #계산을 하고 메모이제이션 배열에 저장
    return memo[n]   #아니라면 -> 이미 계산된 값이면 -> 메모이제이션 배열에 저장된 값을 리턴

memo = [0,1]        #메모이제이션 초기화
print(fibo1(5))


#DP적용
def fibo2():
    f = [0,1]  #초기화
    for i in range(2,n+1):   #f[2] -> f[n]까지 답을 구하기
        f.append(f[i-1]+f[i-2])
    return f[n]
print(fibo2(5))



print(fibo2(5))