def solution(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        num1, num2 = arr[i], arr[i+1]
        while num1%num2:
            remain = num1%num2
            num1, num2 = num2, remain
            # print(num1,num2)
        # print(num1%num2, num1//num2, (arr[i]*arr[i+1])/num2)
        arr[i+1] = (arr[i]*arr[i+1])/num2
    return arr[-1]