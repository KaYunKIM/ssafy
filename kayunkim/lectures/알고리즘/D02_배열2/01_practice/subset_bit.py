#<<연산자 : 피연산자의 비트열을 왼쪽으로 이동시킴
#1<<n : 원소가 n인 경우 n만큼 이동

# print(1<<1)
# print(1<<2)
# print(1<<3)

# &연산자 : 비트연산자
print(10&7)

#10을 2진수로?
#10은 16보다 작고 8보다 큼 -> 2^4는 안되고 2^3은 포함가능
#2^3 + 2^1 => 1010


#7을 2진수로?
0111

arr = [1,2,3]
n = 3
for i in range(1<<n):   # 1<<3 : 8  => range(8)
    print("i: ",i)
    for j in range(n):
        # print(i&(1<<j))
        if i&(a<<j):
            print(arr[j]. end = '')
        print()

#연습문제_ 부분집합의 합
data = [-7,-3,-2,5,8]
n = len(data)
ans = False
for i in range(1<<n):
    sum  = 0
    for j in range(n):
        if i&(1<<j):
            sum += data[j]
    if sum == 0:
        ans = True
print(ans)


