N = int(input())
minV = 1000000000
check = N
while check>N//2:
    sumup = 0
    num = check
    while num>0:
        sumup+=num%10
        num //=10
    if check+sumup ==N and check< minV:
        minV = check
    check-=1
print(minV if minV !=1000000000 else '0')



# N = input()
# minV = 100000000
# if len(N)==1:
#     print('0')
# else:
#     for i in range(int(N)-1,int(N)//2,-1):
#         sumV = i
#         for j in range(len(str(i))):
#             sumV+=int(str(i)[j])
#             if sumV >int(N):
#                 break
#         if sumV == int(N) and i < minV:
#             minV = i
#     if minV == 100000000:
#         print('0')
#     else:
#         print(minV)