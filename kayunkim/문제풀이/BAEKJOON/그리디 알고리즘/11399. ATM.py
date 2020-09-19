N = int(input())
people = list(map(int,input().split()))
people.sort()
ans = 0
for i in range(len(people)):
    ans+=people[i]*(len(people)-i)
print(ans)