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
    start = len(people)-1
    for i in people:
        # print(people.index(i),start)
        for j in range(start,len(people)//2-1,-1):
            ans+=1
            if i+people[j] <= limit:
                start-=1
            break
        if people.index(i)>= start:
            break
    return ans