T = int(input())
lst = list(map(int,input().split()))
a = len(lst)
while a != 1:
    max = lst[0]
    for i in range(1,a):
        if max < lst[i]:
            max = lst[i]
        else:
            lst[i], lst[i-1] = lst[i-1], lst[i]
    a -= 1

while len(lst) != 0:
    print(lst.pop())