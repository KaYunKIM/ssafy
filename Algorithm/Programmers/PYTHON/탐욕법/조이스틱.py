# def solution(name):
#     answer = -1
#     cur = ord('A')
#     if 'A' in name:
#         answer+=min(ord(name[0])-65, 90-ord(name[0])+1)
#         answer+=1
#         for i in range(len(name)-1,0,-1):
#             if name[i] != 'A':
#                 answer+=min(ord(name[i])-65, 90-ord(name[i])+1)
#                 answer+=1
#             else:
#                 answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
#     else:
#         for i in range(len(name)):
#             answer+=min(ord(name[i])-65, 90-ord(name[i])+1)
#             answer+=1
#     return answer


def solution(name):
    answer = 0
    start = list('A' * (len(name) - 1))
    idx = 0
    while True:
        answer += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]))
        start[idx] = name[idx]

        if start == name:
            return answer

        left, right = 1, 1
        for i in range(1, len(name)):
            if name[idx - i] == 'A':
                left += 1
            else:
                break

        for i in range(1, len(name)):
            if name[idx + 1] == 'A':
                right += 1
            else:
                break

        if left > right:
            idx += right
        else:
            idx -= left
        answer += min(left, right)