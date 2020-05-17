def merge(s,e):
    global cnt
    while s or e:
        if s and e:
            if s[-1] >= e[-1]:
                bin.insert(0, s.pop())
            else:
                bin.insert(0, e.pop())
                cnt += 1
        else:
            if len(s)==0:
                bin.insert(0, e.pop())
            elif len(e)==0:
                bin.insert(0, s.pop())

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    start = lst[0:N//2]
    end = lst[N//2:N]
    cnt = 0
    bin=[]
    merge(start,end)
    bin.sort()
    print('#{} {}'.format(tc,bin[N//2],cnt))










# def merge_sorted(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#
#         l = merge_sorted(left)
#         r = merge_sorted(right)
#         return merge(l, r)
#     else:
#         return arr
#
#
# def merge(left, right):
#     i = 0
#     j = 0
#     arr = []
#
#     while (i < len(left)) & (j < len(right)):
#         if left[i] < right[j]:
#             arr.append(left[i])
#             i += 1
#         else:
#             arr.append(right[j])
#             j += 1
#     while (i < len(left)):
#         arr.append(left[i])
#         i += 1
#     #
#     while (j < len(right)):
#         arr.append(right[j])
#         j += 1
#
#     return arr
#
# arr = [3, 5, 1, 2, 9, 6, 4, 5, 7]
# print(merge_sorted(arr))