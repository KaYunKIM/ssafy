def solution(people, limit):
    ans = 0
    people.sort(reverse=True)
    heavy = 0
    light = len(people)-1
    while heavy <= light:
        if people[heavy]+people[light]<=limit:
            light-=1
        ans+=1
        heavy+=1
    return ans



##실패
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






