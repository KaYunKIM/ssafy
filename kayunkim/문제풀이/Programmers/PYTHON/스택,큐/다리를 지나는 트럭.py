# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     on = []
#     finish = []
#     bin = [0]*len(truck_weights)
#     t=0
#     while t != len(truck_weights)-1:
#         if bin[t] == bridge_length:
#             finish.append(on.pop(0))
#             t+=1
#         print('t',t)
#         if sum(on)+truck_weights[t]<=weight:
#             on.append(truck_weights[t])
#         for i in range(t+1):
#             bin[i]+=1
#         print(on, bin)
# #         if cnt==bridge_length:
# #             finish.append(on.pop(0))
# #             cnt -= 1
# #         if sum(on)+t<=weight:
# #             on.append(t)
#
# #         else:
# #             answer+=1
# #             if sum(on)+t<=weight:
# #                 on.append(t)
# #         cnt+=1
# #         answer+=1
#     return answer

# def solution(bridge_length, weight, truck_weights):
#     answer = 1
#     on = []
#     finish = []
#     for t in truck_weights:
#         cnt=0
#         while finish != truck_weights:
#             if cnt==bridge_length:
#                 finish.append(on.pop(0))
#                 cnt = 0
#             if sum(on)+t<=weight:
#                 on.append(t)
#             else:
#                 cnt+=1
#                 on.append(t)
#             cnt+=1
#             print(answer)
#     return answer


import copy

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     on = []
#     fin = []
#     rep = copy.deepcopy(bridge_length)
#     v = [0]*len(truck_weights)
#     h = 0
#     while fin != truck_weights:
#         bridge_length = rep
#
#         # while bridge_length != 0:
#             print(answer,fin,on, bridge_length)
#             if sum(on) + truck_weights[h] <= weight:
#                 on.append(truck_weights[h])
#                 for i in range(h+1):
#                     v[i]+=1
#             bridge_length -= 1
#             answer+=1
#
#         print(answer,fin,on,v)
#         fin.append(on.pop(0))
#         h += 1

def solution(bridge_length, weight, truck_weights):
    on = []
    fin = []
    v = [0]*len(truck_weights)
    h=0
    while fin != truck_weights:
        if h<len(truck_weights):
            if sum(on)+truck_weights[h] <= weight:
                on.append(truck_weights[h])
                h+=1
        for i in range(h):
            v[i]+=1
        print(h, fin, on, v)
        if bridge_length in v:
            fin.append(on.pop(0))
        print('ans', h, fin, on, v)
        if h==len(truck_weights):
            v[0] += bridge_length
            return v[0]
    print(fin,v[0]+1)

print(solution(2,10,[7,4,5,6]))



def solution(bridge_length, weight, truck_weights):
    on = []
    fin = []
    v = [0]*len(truck_weights)
    h=0
    while fin != truck_weights:
        if h<len(truck_weights):
            if sum(on)+truck_weights[h] <= weight:
                on.append(truck_weights[h])
                h+=1
        for i in range(h):
            v[i]+=1
        if bridge_length in v:
            fin.append(on.pop(0))
    return v[0]+1


def solution(bridge_length, weight, truck_weights):
    on = []
    cnt = 0
    sumV=0
    while truck_weights:
        cnt += 1
        if sumV+truck_weights[0]<=weight:
            on.insert(0,truck_weights.pop(0))
            sumV+=on[0]
        else:
            on.insert(0,0)
        if len(on)==bridge_length:
            sumV-=on.pop()
    return cnt+bridge_length