# import copy
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     on = []
#     finished = []
#     B = copy.deepcopy(bridge_length)
#     print(bridge_length)
#     while len(truck_weights)!=0 and len(on) !=0:
#
#         # if sum(on) + truck_weights[0] <= weight:
#         #     on.append((truck_weights.pop(0))
#         print(bridge_length)
#         # bridge_length-=1
#         # if bridge_length == 0:
#         #     finished.append(on.pop(0))
#         # bridge_length = B
#         # answer += 1
#     return answer
#
# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]
# solution(bridge_length, weight, truck_weights)


def solution(bridge_length, weight, truck_weights):
    answer = 1
    on = []
    finish = []
    for t in truck_weights:
        cnt=0
        while finish != truck_weights:
            if cnt==bridge_length:
                finish.append(on.pop(0))
                cnt = 0
            if sum(on)+t<=weight:
                on.append(t)
            else:
                cnt+=1
                on.append(t)
            cnt+=1
            print(answer)
    return answer