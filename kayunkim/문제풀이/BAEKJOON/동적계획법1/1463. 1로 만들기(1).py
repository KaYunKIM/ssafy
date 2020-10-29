def find(num,sumV):
    global minV
    if num == 1:
        if sumV< minV:
            minV = sumV
            return
    else:
        if sumV > minV:
            return
        else:
            if num%3==0:
                find(num//3,sumV+1)
            if num%2==0:
                find(num//2, sumV+1)
            find(num-1, sumV+1)

N = int(input())
minV = 100000000000
find(N,0)
print(minV)