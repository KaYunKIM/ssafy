# import heapq
# def solution(people, limit):
#     sumV = 0
#     cur = 0
#     cnt = 0
#     while people:
#         heapq.heapify(people)
#         if sumV + people[0] <= limit:
#             sumV+= people.pop(0)
#             cur+=1
#             # print('1',people, sumV, cnt)
#         else:
#             sumV = 0
#             cnt+=1
#         if cur == 2:
#             sumV = 0
#             cnt+=1
#             # print('2',people, sumV, cnt)
#     return cnt+1


def solution(people, limit):
    ans = 0
    people.sort(reverse=True)
    for i in people:
        for j in range(len(people) - 1, len(people) // 2 - 1, -1):

    return ans