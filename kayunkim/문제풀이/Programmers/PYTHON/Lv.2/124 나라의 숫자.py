# def solution(n):
#     answer = []
#     temp = [4,1,2]
#     while n>2:
#         answer.insert(0,temp[n%3])
#         print('1',answer)
#         n//=3
#         print('1',n)
#     if n!=0:
#         print(n)
#         answer.insert(0,temp[n])
#         print('2',answer)
#     return answer

def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
