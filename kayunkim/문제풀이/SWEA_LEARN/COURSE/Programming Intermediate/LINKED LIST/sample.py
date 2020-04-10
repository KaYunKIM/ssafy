arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

# for i in range(1, N):        #1~N -1
#     temp = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] >temp:
#         arr[j+1] = arr[j]
#         j-=1
#     arr[j+1] = temp
#
#     print(arr)

for i in range(1,N):
    temp = arr[i]
    j = i-1
    while j>= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        arr[j] = temp
        j -= 1

    print(arr)
