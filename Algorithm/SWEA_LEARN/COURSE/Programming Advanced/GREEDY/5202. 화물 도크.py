T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    for i in time:
        i[0],i[1] = i[1],i[0]
    time.sort()
    cnt = 1
    first = time[0][0]
    for i in time:
        if i[1]>= first:
            cnt+=1
            first = i[0]
    print('#{} {}'.format(tc,cnt))

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     time = [list(map(int,input().split())) for _ in range(N)]
#     print(time)
#     time.sort(key=lambda x:x[1])
#     first = time[0][1]
#     cnt = 1
#     for t in time:
#         if first <= t[0]:
#             print(first,t, t[0])
#             first = t[1]
#             cnt+=1
#     print('#{} {}'.format(tc,cnt))