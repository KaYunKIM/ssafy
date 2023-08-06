# def binarySearch(a, Key):
#     start = 0
#     end = len(a)-1
#     cnt =0
#     while start <= end:
#         middle = (start+end)//2
#         if a[middle] == key:
#             return True, cnt
#         elif a[middle] > key:
#             end = middle-1
#         else:
#             start = middle+1
#         cnt += 1
#     return False, cnt
#
# key = 7
# arr = [2,4,7,9,11,19,23]
# print(binarySearch(arr,7))

## 재귀방법
def binarySearch2(a,low,high,key):
    if low > high:
        return False
    else:
        middle = (low+high)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            binarySearch2(a,low,middle-1,key)
        else:
            binarySearch2(a,middle+1,high,key)



arr = [2,4,7,9,11,19,23]
print(binarySearch(arr,0,len(arr)-1,7))

