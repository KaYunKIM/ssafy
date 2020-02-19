#1
lst = list(map(int,input().split()))

sum = 0
cnt = 0
for j in lst:
    if 0 <= j <= 100:
        sum+= j
        cnt+= 1
        avg = round(sum/cnt,1)
    else:
        print('sum : {}\navg : {}'.format(sum,avg))

#2
lst = list(map(int, input().split()))

sum = 0
cnt = 0
i = 0
while i < len(lst) - 1:
    if lst[i] <= 100:
        sum += lst[i]
        cnt += 1
        avg = round(sum / cnt, 1)

    else:
        break
    i += 1
print('sum : {}\navg : {}'.format(sum, avg))