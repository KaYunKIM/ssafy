a = input().split()
ls = []
for i in range (len(a)):
    ls.append(a[i])

sum_even = 0
sum_odd=  0

for i in range(len(a)):
    if i%2==1:
        sum_even+= int(ls[i])
    if i%2==0:
        sum_odd += int(ls[i])
        avg1 = sum_odd/5

print('sum : ' + str(sum_even))
print('avg : ' + str(round(avg1,1)))



# arr = list(map(int,input().split()))
# sum_even = sum_odd = 0
# for i in range(len(arr)):
#     if (i+1)%2 == 0:
#         sum_even+= arr[i]
#     else:
#         sum_odd+= arr[i]
#
# print('sum: {}'.format(sum_even))
# print('avg: {}'.format(sum_odd/5))