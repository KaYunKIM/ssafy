N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
temp = [house[0][0], house[0][1], house[0][2]]
for i in range(1,N):
    house[i][0]+= min(temp[1], temp[2])
    house[i][1]+= min(temp[0], temp[2])
    house[i][2]+= min(temp[0], temp[1])
    temp = [house[i][0], house[i][1], house[i][2]]
print(min(house[-1]))