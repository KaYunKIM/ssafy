def merge_sort(m):
    if len(m) <=1:   #size가 0이거나 1인 경우, 바로 리턴
        return m

    #1. DIVIDE 부분
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    # 리스트의 크기가



def merge(left, right):
    result = []

    while len(left) >0 and len(right) >0:

        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left)>0:
        result.extend(left)
    if len(right)>0:
        result.extend(right)
    return return