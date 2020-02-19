T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    maxV = -1       #최대값을 찾기 위한 변수
    for i in range(len(arr)):
        for j in range(len(arr)):
            num = arr[i]*arr[j]
            if i < j and maxV < num:    #문제에서 주어진 조건에 만족할 때만 계산
                #현재까지 찾은 최대값 보다 수가 클 때만 단조증가 체크
                num_copy = num
                pre = 10
                while num:
                    n = num%10
                    if pre < n:
                        islnc = False
                        break
                    num = num//10
                    pre = n
                #최대값 찾기
                if islnc:   #단조 증가할 때만
                    if maxV < num_copy:
                        maxV = num_copy:

            #print(num)