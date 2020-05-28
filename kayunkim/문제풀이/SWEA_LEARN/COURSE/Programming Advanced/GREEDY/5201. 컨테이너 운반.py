# T = int(input())
# for tc in range(1,T+1):
#     N,M = list(map(int,input().split()))
#     container = list(map(int,input().split()))
#     truck = list(map(int,input().split()))
#     container.sort(reverse=True)
#     truck.sort(reverse=True)
#     cnt = 0
#     h = min(N,M)
#     while h !=0:
#         if container[0]> truck[0]:
#             container.pop(0)
#         else:
#             cnt+=container[0]
#             container.pop(0)
#             truck.pop(0)
#         h-=1
#     print('#{} {}'.format(tc,cnt))


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    cargo = list(map(int,input().split()))   #N개
    capacity = list(map(int, input().split()))   #M개
    cargo.sort(reverse=True)
    capacity.sort(reverse=True)
    cnt = 0
    while cargo and capacity:
        if cargo[0] <= capacity[0]:
            cnt+=cargo.pop(0)
            capacity.pop(0)
        else:
            cargo.pop(0)
    print('#{} {}'.format(tc,cnt))