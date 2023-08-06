T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input()))
    lst1 = [0]*10
    for i in lst:
        lst1[i] +=1
    max = 0
    max1 = 0
    for i in range(len(lst1)):
        if max <= lst1[i]:
            max = lst1[i]
            if max1 < i:
                max1 = i
    print('#{} {} {}'.format(tc,max1,max))