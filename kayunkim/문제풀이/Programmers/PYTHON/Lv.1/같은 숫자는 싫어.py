def solution(arr):
    answer = []
    cur = -1
    for i in arr:
        if cur != i:
            answer.append(i)
            cur = i
    return answer