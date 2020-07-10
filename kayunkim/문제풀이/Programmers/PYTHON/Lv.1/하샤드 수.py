def solution(x):
    arr= [int(i) for i in str(x)]
    if x%sum(arr)!=0:
        return False
    return True