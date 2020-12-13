def solution(arr):
    answer = 0
    temp = 0
    arr.sort(reverse=true)
    for i in range(len(arr) - 1):
        num1, num2 = arr[i], arr[i + 1]
        while num1 % num2:
            remain = num1 % num2  # 6
            arr[i] = arr[i + 1]
    return answer