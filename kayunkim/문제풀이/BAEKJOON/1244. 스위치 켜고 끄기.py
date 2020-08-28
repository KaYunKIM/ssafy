N = int(input())
switch = list(map(int,input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int,input().split())
    if sex == 1:
        for i in range(num-1,N,num):
            switch[i] = 1 - switch[i]
        print(1,switch)
    else:
        next=0
        while switch[num-2-next] == switch[num-2+next] and num-2-next>=0 and num-2+next<=N-1:
            next+=1
        print(next, num-1-next, num-1+next)
        for i in range(num-1-next,num+next):
            switch[i] = 1 - switch[i]
            print(2,switch)
for i in range(0,N,20):
    print(*switch[i:i+20])



# T = int(input())
# arr_1 = list(map(int, input().split()))
# N = int(input())
# arr_2 = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     if arr_2[i][0] == 1:
#         for j in range(arr_2[i][1] - 1, T, arr_2[i][1]):
#             arr_1[j] = 1 - arr_1[j]
#     elif arr_2[i][0] == 2:
#         while True:
#             cnt = 0
#             for j in range(1, T):
#                 if arr_2[i][1] + j - 1 < T and arr_2[i][1] - j - 1 >= 0:
#                     if arr_1[arr_2[i][1] - j - 1] == arr_1[arr_2[i][1] + j - 1]:
#                         cnt += 1
#                     else:
#                         break
#             break
#         if cnt == 0:
#             arr_1[arr_2[i][1] - 1] = 1 - arr_1[arr_2[i][1] - 1]
#         else:
#             for k in range(arr_2[i][1] - cnt - 1, arr_2[i][1] + cnt):
#                 arr_1[k] = 1 - arr_1[k]
# if T <= 20:
#     for i in range(T):
#         print(arr_1[i], end = ' ')
# else:
#     for j in range(T):
#         print(arr_1[j], end = ' ')
#         if (j + 1) % 20 == 0 and j != 0:
#             print()