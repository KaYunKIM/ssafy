# def hwaduk():
#     global queue
#     if len(newpizza) != 0:
#         while len(queue)!= N:
#             a = newpizza.pop(0)
#             queue.append(a)
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = list(map(int,input().split()))
#     pizza = list(map(int,input().split()))
#     newpizza = pizza[::]
#     queue = []
#     hwaduk()
#     while len(queue) != 1:
#         ans = queue.pop(0)
#         if ans == 0:
#             hwaduk()
#         if ans != 0:
#             for idx, val in enumerate(pizza):
#                 if ans == val:
#                     ansidx = idx
#                     queue.append(pizza[ansidx]//2)
#     print(queue[0],ansidx)
#     # print(queue[0])


T = int(input())
N,M = list(map(int,input().split()))
    pizza = list(map(int,input().split()))
    queue = []
    for idx,val in enumerate(pizza):
        queue.append((idx,val))
    while queue:
        a = queue.pop(0)
        if a[1]//2 != 0:
            queue.insert(N-1,(a[0],a[1]//2))
        if len(queue) ==1:
            ans = queue[0][0]
    print('#{} {}'.format(tc,ans+1))