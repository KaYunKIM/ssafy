T = int(input())
for tc in range(1, T + 1):
    t,N = input().split()
    N = int(N)
    nums = ['ZRO','ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    counts = [0 for i in range(10)]  #수를 카운팅하기 위한 배열
    arr = input().split()            #입력을 받아서 배열에 저장
    for i in range(len(arr)):
        for j in range(len(nums)):
            if arr[i] == nums[j]:
                counts[j]+=1
    print(t)
    for i in range(len(counts)):
        for j in range(counts[i]):
            print(nums[i], end= ' ')
    print()