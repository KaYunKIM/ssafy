def solve(arr1, arr2):
    len1 = lrn(arr1)
    len2 = len(arr2)
    maxV = 0

    for i in range(0, len2 - len1 + 1):
        sum = 0
        for j in range(0, len1):
            num = arr[j]*arr2[i+j]
            sum += num
