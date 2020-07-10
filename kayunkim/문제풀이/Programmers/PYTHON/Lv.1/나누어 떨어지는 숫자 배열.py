def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor==0]) or [-1]

    # answer = []
    # for i in arr:
    #     if i%divisor==0:
    #         answer.append(i)
    # if not answer:
    #     answer = [-1]
    # return sorted(answer)