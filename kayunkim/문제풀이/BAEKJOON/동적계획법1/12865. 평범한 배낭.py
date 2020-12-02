# N,K = map(int,input().split())
# bag = [list(map(int,input().split())) for _ in range(N)]
# maxV = [0]*N
# weight = [0]*N
# for i in range(N):
#     if i == 0:
#         weight[i] = bag[i][0]
#         maxV[i] = bag[i][1]
#     else:
#         if maxV[-1]+bag[i][0] <= K:
#             w = maxV[-1]+bag[i][0]
#             m = maxV[-1] + bag[i][1]
#         else:
#             if i == 1:
#                 w = max(weight[-1])
#                 maxV[i] = maxV[-1]
#             else:
#                 w = max(weight[-1])
#                 maxV[i] = maxV[-1]


#       3  4  5  6
#       6  8  12  13
#
# xx    0 0  6  14
# xo    0 8  18 27
# ox    6 6  14 26
# oo    6 14 26 39

N, K = map(int,input().split())
bags = []
for _ in range(N):
    W,V = map(int,input().split())
    bags.append([W,V])
bags.sort()
print(bags)
temp = []
if bags[0][0] <= K:
    temp.append(bags[0][1])
if bags[1][0] <= K:
    temp.append(max(bags[1][1], temp[-1]+bags[1][1]))
for i in range(2,len(bags)):
    maxV = []
    maxV.append(temp[-2])
    maxV.append(temp[-1])
    if bags[-2][0]+bags[i][0]<=K:
        maxV.append(temp[-2]+bags[i][1])
    if bags[-1][0] + bags[i][0] <= K:
        maxV.append(temp[-1]+bags[i][1])
    print('maxV',maxV)
    temp.append(max(maxV))
    print(temp)
print(temp[-1])