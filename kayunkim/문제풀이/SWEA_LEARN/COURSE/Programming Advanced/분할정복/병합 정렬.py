def merge(k):
    if k == N//2:
        return
    else:
        while len(start)!=0 and len(end)!=0:
            # if len(start)==len(end):
            if start[-1] < end[-1]:
                bin.append(start.pop())
            else:
                bin.append(end.pop(0))
            # elif len(start) < len(end):
            print(bin)
        k+=1



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    start = num[0:N//2]
    end = num[N//2:N]
    print(start, end)
    bin = []
    merge(0)
    print(bin)

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
#     # ㅇㅇㅇ
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