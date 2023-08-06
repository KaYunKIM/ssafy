## 실패
# maxV = 0
# v = [0]*4

# def find(level,sumV, land):
#     global maxV
#     if level == len(land):
#         if sumV > maxV:
#             maxV = sumV
    
#     if level < len(land):
#         for j in range(4):
#             if not v[j]:
#                 v[j] = 1
#                 find(level+1, sumV+land[level][j], land)
#                 v[j] = 0
#     return

# def solution(land):
#     global maxV
#     find(0,0,land)
#     return maxV



def solution(land):
    for i in range(len(land)-1):
        maxV = [0]*4
        for k in range(4):
            temp = []
            for j in range(4):
                if j != k:
                    temp.append(land[i+1][k]+land[i][j])
            land[i+1][k] = max(temp)
                        
    return max(land[-1])



## 시간 단축
def solution(land):
    for i in range(len(land)-1):
        for j in range(4):
            land[i+1][j]+= max(land[i][:j]+land[i][j+1:])
    
    return max(land[-1])