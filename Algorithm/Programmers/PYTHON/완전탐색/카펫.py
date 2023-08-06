def solution(brown, yellow):
    plus = (brown+4)//2
    mul = yellow + 2*plus-4
    a = min(plus,mul)
    for i in range(1,a//2+1):
        if i*(plus-i)==mul:
            answer = [i,plus-i]
            break
    answer.sort(reverse=True)
    return answer

# 실패
# def solution(brown, yellow):
#     answer = []
#     if yellow > 4:
#         width = yellow//4+2
#     else:
#         width = yellow%4+2
#     answer.append(width)
#     height = brown//2 - width +2
#     answer.append(height)
#     answer.sort(reverse=True)
#     return answer