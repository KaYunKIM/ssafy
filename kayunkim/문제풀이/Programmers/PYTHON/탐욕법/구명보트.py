# # import heapq
# def solution(people, limit):
#     answer = 0
#     # for i in range(0,len(people)-1):
#     while len(people):
#         maxV = 0
#         if limit-people[0]<40:
#             answer+=1
#         elif people[0]!=0:
#             for j in range(1,len(people)):
#                 if maxV< people[j] <= limit-people[0]:
#                     maxV, cur = people[j], j
#             if maxV != 0:
#                 people.remove(people[cur])
#             answer+=1
#         # people = people
#     if people[-1]!=0:
#         answer+=1
#     return answer


import heapq
def solution(people, limit):
    sumV = 0
    cur = 0
    cnt = 0
    while people:
        heapq.heapify(people)
        if sumV + people[0] <= limit:
            sumV+= people.pop(0)
            cur+=1
            # print('1',people, sumV, cnt)
        else:
            sumV = 0
            cnt+=1
        if cur == 2:
            sumV = 0
            cnt+=1
            # print('2',people, sumV, cnt)
    return cnt+1