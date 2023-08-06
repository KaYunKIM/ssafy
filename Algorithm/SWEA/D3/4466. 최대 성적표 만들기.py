T = int(input())
for tc in range(1,T+1):
    N,K = list(map(int,input().split()))
    score = list(map(int,input().split()))
    cnt = 0
    while K!=0:
        max = 0
        for i in score:
            if max<i:
                max = i
        cnt+=max
        score.remove(max)
        K-=1
    print(cnt)


#시간초과
# T = int(input())
# for tc in range(1,T+1):
#     N,K = list(map(int,input().split()))
#     score = list(map(int,input().split()))
#     max = 100
#     min = 0
#     bin = []
#     while len(bin)!=K:
#         for i in score:
#             if i == max:
#                 bin.append(i)
#             if min<i and i<max:
#                 min = i
#         max = min
#         min = 0
#     print('#{} {}'.format(tc,sum(bin)))