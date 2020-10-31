N = int(input())
find = [0]*(N+1)
for i in range(2, N+1):
    temp = []
    if i%3 == 0:
        temp.append(find[i//3]+1)
    if i%2 == 0:
        temp.append(find[i//2]+1)
    temp.append(find[i-1]+1)
    find[i] = min(temp)
print(find[-1])


# def find(num,sumV):
#     global minV
#     if num == 1:
#         if sumV< minV:
#             minV = sumV
#             return
#     else:
#         if sumV > minV:
#             return
#         else:
#             if num%3==0:
#                 find(num//3,sumV+1)
#             if num%2==0:
#                 find(num//2, sumV+1)
#             find(num-1, sumV+1)
#
# N = int(input())
# minV = 100000000000
# find(N,0)
# print(minV)