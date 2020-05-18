def merge(A):
    global cnt
    if len(A)==1:
        return A
    else:
        start = A[:len(A)//2]
        end = A[len(A)//2:]
        start = merge(start)
        end = merge(end)
        idxl = 0
        idxr = 0
        i= 0
        while idxl < len(start) and idxr < len(end):
            if start[0] > end[0]:
                A[i] = end[0]
                end.pop(0)
            else:
                A[i]= start[0]
                start.pop(0)
            i+=1

        if start[-1] > end[-1]:
            cnt+=1
        if len(start)==0:
            A[i:] = end
        elif len(end)==0:
            A[i:] = start
        return A

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    bin=[]
    merge(lst)
    print('#{} {}'.format(tc,bin[N//2],cnt))

# def merge(a):
#     global cnt
#     if len(a) == 1:
#         return a
#     else:
#         m = len(a)//2
#         left = a[:m]
#         right = a[m:]
#         left = merge(left)
#         right = merge(right)
#         idxl = 0
#         idxr = 0
#         i = 0
#         while idxl < len(left) and idxr < len(right):   #좌/우 리스트에 비교 대상이 남을때까지
#             if left[idxl] < right[idxr] :       #작은 값을 a 배열에
#                 a[i] = left[idxl]
#                 idxl +=1
#             else:
#                 a[i] = right[idxr]
#                 idxr +=1
#             i+=1
#         if left[-1] > right[-1]:    #왼쪽의 마지막 원소가 오른쪽의 마지막 원소보다 클경우
#             cnt+=1
#         if idxl < len(left):    #왼쪽 리스트가 남은경우   -> 남은 원소를 a 배열에
#             a[i:] = left[idxl:]
#         if idxr< len(right):    #오른쪽 리스트가 남은경우
#             a[i:] = right[idxr:]
#         return a
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     A = list(map(int,input().split()))
#     cnt = 0
#     A = merge(A)
#     print('#{} {} {}'.format(tc,A[N//2],cnt))







## 병합정렬 알고리즘
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