#이진탐색 구현

'''
검색 시작점, 종료점을 설정함 (반복이 진행되면서 시작점, 종료점 갱신)
반복 시작
    시작점이 종료점보다 커진다면, 더 이상 탐색 불가하므로 반복 종료
    중앙값 구함
    중앙점의 값과 찾고자 하는 값 비교해봄
        같다면? => 찾았으니깐 True 리턴
        중앙점의 값이 크다면?  왼쪽탐색 => 종료점을 갱신
        작다면? 오른쪽 탐색 => 시작점을 갱신
반복 종료 후 아직도 리턴을 못했다면? 없다는 의미이므로 False 리턴
'''


def binarySearch(a.key):
    start = 0
    end  len(a) -1
    while True:
        middle = (start+end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle+1
    return False
arr = [2,4,7,9,11,19,23]
for i in range(len(arr)):
    if arr[len(arr)//2] > arr[i]:


#선택정렬 구현
def selectionSort():
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]     #탐색구간의 가장 앞이랑 최소값을 바꿈

arr = [5,3,2,1,4]
selectionSort(arr)
print(arr)