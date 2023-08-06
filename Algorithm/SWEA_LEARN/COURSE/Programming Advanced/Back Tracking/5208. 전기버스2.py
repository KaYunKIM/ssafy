#cur = 현재위치
#sum = 충전횟수
#battery = 잔여 배터리

def charge(cur,battery,sum):
    global bus_stop, minV, ans
    if cur == bus_stop:
        if sum < minV:
            minV = sum
        return
    else:
        if sum > minV:
            return
        else:
            #충전하고 지나가기
            charge(cur+1, lst[cur]-1, sum+1)
            #충전 안하고 지나가기
            if battery>0:
                charge(cur+1, battery-1, sum)


T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    bus_stop = lst[0]
    minV = 10000
    charge(2,lst[1]-1,0)
    print('#{} {}'.format(tc,minV))

# def charge(cur,sum,battery):
#     global minV
#     if cur == N:
#         if sum < minV:
#             minV = sum
#         return
#     else:
#         if sum> minV:
#             return
#         else:
#             for i in range(1,N):
#                 if v[i]==0:
#                     v[i]=1
#                     if battery>0:
#                         charge(cur+1,sum,lst[i]-1)
#                     charge(cur+1, sum+1, lst[i])
#                     v[i]=0
#
#
# T = int(input())
# for tc in range(1,T+1):
#     lst = list(map(int,input().split()))
#     N = lst[0]
#     minV = 1000000
#     v = [0]*N
#     charge(1,0,lst[1])
#     print(minV)