# def solution(numbers):
#     answer= 0
#     i = 0
#     while numbers:
#         max,first = 0,0
#         for n in numbers:
#             if first <= int(str(n)[0]) or max < int(str(n)):
#                 max, first = n, int(str(n)[0])
#         print('max',max)
#         # print(numbers.pop())
#         numbers.remove(max)
#     return answer
#
#
#
#
# def solution(numbers):
#     for n in numbers:
#         temp = sorted(numbers,key = lambda n:str(n)[0], reverse=True)
#     return (''.join(map(str,temp)))


def solution(numbers):
    numbers = list(map(str,numbers))
    # temp = sorted(num, key = lambda x:x[0], reverse=True)
    numbers.sort(key=lambda x: x*3, reverse=True)
    return ''.join(numbers)