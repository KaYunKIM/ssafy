N = int(input())
people = []
for i in range(N):
    weight, height = map(int,input().split())
    people.append([weight,height,i])
people.sort(reverse=True)
ans = [0]*N
ans[people[0][2]] = 1
for i in range(1,N):
    rank = 0
    h=i-1
    while h >=0:
        if people[h][0] > people[i][0] and people[h][1] > people[i][1]:
            rank+=1
        h-=1
    ans[people[i][2]] = rank+1
print(' '.join(map(str,ans)))