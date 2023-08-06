# def find(cur, friends):
#     queue = friends  #2중배열 => pop을 2번한다 => 친구 찾기 가능  #[[2,3]]
#     invitation=set([])  #초대 받은 친구들
#     while queue:  #한 단계 다 보
#         temp = [] #친구의 친구 배열
#         next = queue.pop(0)  #[2,3]// [1,3]&[1,4,2]
#         while next:
#             print(next)
#             friend_num = next.pop(0)
#             invitation.add(friend_num)
#             temp.extend(arr[friend_num])
#             print('temp', temp)
#         queue = [temp]
#         cur+=1
#         print(invitation)
#         if cur ==3:
#             return len(invitation)-1
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     arr={i:[] for i in range(N+1)}
#     for _ in range(M):
#         a,b = map(int,input().split())
#         arr[a].append(b)
#         arr[b].append(a)
#     print(arr)
#     if arr[1]:
#         ans = find(1,[arr[1]])
#     else:
#         ans = 0
#     print('#{} {}'.format(tc,ans))

def find(start):
    queue = [start]
    invitation[start]=1
    while queue:
        friend = queue.pop(0)
        for next in arr[friend]:
            if invitation[next]==0:
                queue.append(next)
                invitation[next] = invitation[friend]+1
        if invitation[friend]==3:
            return

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = {i:[] for i in range(N+1)}
    for _ in range(M):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    print(arr)
    invitation = [0]*(N+1)
    find(1)
    ans = invitation.count(2)+invitation.count(3)
    print('#{} {}'.format(tc,ans))