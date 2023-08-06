def solution(heights):
    answer = [0]*len(heights)
    for i in range(1,len(heights)):
        h = i
        while h!=0:
            if heights[h-1]> heights[i]:
                answer[i]=h
                break
            h-=1
    return answer


# def solution(heights):
#     answer = [0]*len(heights)
#     for i in range(len(heights)-1,0,-1):
#         for j in range(i-1,-1,-1):
#             if heights[j]> heights[i]:
#                 answer[i]=j+1
#                 break
#     return answer