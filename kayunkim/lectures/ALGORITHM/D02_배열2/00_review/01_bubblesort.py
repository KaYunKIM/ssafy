arr = [5,2,3,4,1]

init = arr[0]
for i in range(len(arr)):
    if init> arr[i]:
        init, arr[i] = arr[i], init

    print(arr)