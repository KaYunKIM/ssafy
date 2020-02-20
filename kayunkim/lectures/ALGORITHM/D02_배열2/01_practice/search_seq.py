#a : 배열
#n : 배열의 길이
#key : 찾고자 하는 수
def seqSearch(a,n,key):
    i = 0
    while i < n and a[i] != key:
        i+=1
    if i < n : return i
    else: return -1

arr = [4,9,11,23,2,19,7]        #정렬이 안되어 있음
print(seqSearch(arr, len(arr), 2))
print(seqSearch(arr,len(arr),8))    #찾는 값이 없으면 -1리턴
arr = [1,2,3,4,5,6,7]       #정렬되어 있는 경우

