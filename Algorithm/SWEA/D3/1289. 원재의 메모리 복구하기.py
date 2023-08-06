# T = int(input())
# for tc in range(1,T+1):
#     org = list(map(int,input()))
#     cnt = 0
#     ans = []
#     if org[0] == 1:
#         cnt+=1
#     for i in range(len(org)-1):
#         if org[i] != org[i+1]:
#             cnt+=1
#     print('#{} {}'.format(tc,cnt))

T = int(input())
for tc in range(1,T+1):
    org = list(map(int,input()))
    cur = org[0]
    cnt = 0
    if org[0] == 1:
        cnt+=1
    for i in range(1,len(org)):
        if cur!= org[i]:
            cnt+=1
            cur = org[i]
    print('#{} {}'.format(tc,cnt))