# 1차 풀
def solution(arr):
    arr.sort()
    for i in range(1, len(arr)):
        temp = 1
        for j in range(2, max(arr[i - 1], arr[i]) + 1):
            while True:
                if arr[i - 1] % j == 0 or arr[i] % j == 0:
                    if arr[i - 1] % j == 0 and arr[i] % j == 0:
                        arr[i - 1] //= j
                        arr[i] //= j
                        temp *= j
                    elif arr[i - 1] % j == 0:
                        arr[i - 1] //= j
                        temp *= j
                    elif arr[i] % j == 0:
                        arr[i] //= j
                        temp *= j
                else:
                    break

            if arr[i - 1] == 1 and arr[i] == 1:
                break

        arr[i] = temp
    return arr[-1]



# 최소공배수 = 두 수의 곱 // 최대공약수
def solution(arr):
    for i in range(1, len(arr)):
        A, B = arr[i - 1], arr[i]
        while A % B:이
            A, B = B, A % B
            print(A, B)
        arr[i] = arr[i - 1] * arr[i] // B

    return arr[-1]

