# def solution(s):
#     stack = [s[0]]
#     h=1
#     while len(s[:h+1])<= len(s[h+1:]):
#         if s[h]==stack[-1]:
#             stack.pop()
#             s=s[:h-1]+s[h+1:]
#             h-=2
#         else:
#             stack.append(s[h])
#         h+=1
#         if not stack:
#             stack = [s[0]]
#             h+=1
#         print(stack,s,h)
#     if not stack:
#         return 1
#     return 0


## 효율성 실패
def solution(s):
    h = 1
    while h < len(s):
        if s[h] == s[h-1]:
            s = s[0:h-1]+s[h+1:]
            if h>1:
                h-=1
        else:
            h+=1
    if not s:
        return 1
    else:
        return 0

## 효율성 통과
def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        return 1
    else:
        return 0