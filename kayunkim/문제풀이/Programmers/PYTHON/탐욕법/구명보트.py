# import heapq
# def solution(people, limit):
#     answer = 0
#     h = 0
#     while people:
#         maxV = 0
#         temp = heapq.heappop(people)
#         if temp!=0:
#             if limit-temp < 40:
#                 answer+=1
#             else:
#                 if len(people)==1:
#                     answer+=1
#                 i=1
#                 cur = 0
#                 # print(temp, people[i])
#                 while heapq.heapify(people):
#                     if maxV < people[i] <= limit-temp:
#                         maxV, cur = people[i],i
#                     i+=1
#                 # print(maxV, cur)
#                 people[cur]=0
#                 # print(people)
#                 answer+=1
#         h+=1
#     return answer
def solution(people, limit):
    answer = 0
    # for i in range(0,len(people)-1):
    while len(people):
        maxV = 0
        if limit-people[0]<40:
            answer+=1
        elif people[0]!=0:
            for j in range(1,len(people)):
                if maxV< people[j] <= limit-people[0]:
                    maxV, cur = people[j], j
            if maxV != 0:
                people.remove(people[cur])
            answer+=1
        # people = people
    if people[-1]!=0:
        answer+=1
    return answer