# i = 0
# while True:
#     if i < 74:
#         if i == 3 or (i-3)%10 == 0 :
#             print(i, end=' ')
#
#         i += 1


i = 0
while True:
    if i %10 != 3:
        i+=1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1





