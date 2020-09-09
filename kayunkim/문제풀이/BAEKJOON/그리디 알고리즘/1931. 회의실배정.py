N = int(input())
timetable = [list(map(int,input().split())) for _ in range(N)]
timetable.sort()
ans = 1
minV = 2**31
for i in range(len(timetable)):
    if timetable[i][1] <= minV:
        minV = timetable[i][1]
    else:
        if timetable[i][0]>= minV:
            ans+=1
            minV = 2**31
            if timetable[i][1] <= minV:
                minV = timetable[i][1]
print(ans)