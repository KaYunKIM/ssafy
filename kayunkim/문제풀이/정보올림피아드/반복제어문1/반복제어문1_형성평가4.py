# while True:
#     T = list(map(int,input().split()))
#     sum = 0
#     for i in T:
#         if i != 0:
#             if i%3 == 0 or i%5 == 0:
#                 continue
#             else:
#                 sum+= 1
#                 print(sum)
        # else:
        #     break
        #     print(sum)


# T = list(map(int,input().split()))
# sum = 0
# for i in T:
#     while i != 0:
#         if i%3 == 0 or i%5 == 0:
#             continue
#         else:
#             sum+= 1
#         print(sum)
#              break
#     else:
#         print(sum)


lst = list(map(int,input().split()))

cnt=0
for i in lst:
    if i == 0:
        break
    if i%3 ==0 or i%5 == 0:
        continue
    else:
        cnt+=1
print(cnt)

