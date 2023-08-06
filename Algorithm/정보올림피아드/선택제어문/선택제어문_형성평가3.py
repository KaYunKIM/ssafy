age = int(input())

if age %400 ==0 or (age%4==0 and age%100 != 0):
    print('leap year')
else:
    print('common year')





# if age%4 == 0:
#     if age%100 == 0:
#         print('leap year')
#     elif age%100 !=0:
#         print('common year')