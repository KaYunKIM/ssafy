cnt = 0
def find(k, sumV,numbers,target):
    global cnt
    if k == len(numbers):
        if sumV == target:
            cnt += 1
            return
    else:
        find(k+1, sumV-numbers[k], numbers, target)
        find(k+1, sumV+numbers[k], numbers, target)

def solution(numbers, target):
    find(0,0,numbers,target)
    return cnt



# def solution(numbers, target):
#     cnt = 0
#     N = len(numbers)
#
#     def find(k, sumV):
#         nonlocal cnt
#         if k == N:
#             if sumV == target:
#                 cnt += 1
#         else:
#             find(k + 1, sumV - numbers[k])
#             find(k + 1, sumV + numbers[k])
#
#     find(0, 0)
#     return cnt