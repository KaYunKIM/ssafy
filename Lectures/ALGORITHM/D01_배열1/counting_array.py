# arr = [0, 4, 1, 3, 1, 2, 4, 1]
# cnt = []
# for i in range(len(arr)):
#     cnt.append(arr[i])


def countingsort(A, B, k):  # A: 정렬할 배열  K: 배열의 최대값
    C = [0] * k  # 카운팅 배열

    for i in range(0, len(A)):  # A배열의 원소 갯수 세기
        C[A[i]] += 1
    # print(C)
    # 카운트 배열 조작하기: 숫자들이 들어갈 자리를 표현하도록 내 앞 인덱스 숫자를 더해서 대입


    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, 0, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    return B

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print(countingsort(arr,[0]*len(arr), 5))