n = 12      #1~12까지의 숫자
arr = [i for i in range(1,n+1)]
#print(arr)

T = int(input())
for tc in range(1,T+1):
    #N : 부분집합의 원소수, K: 부분집합의 총합
    N,K = map(int,input().split())
    result = 0              #문제의 조건에 맞는 경우의 수

    for i in range(1<<n):
        total = 0  # 부분합 개수 체크
        cnt = 0  # 원소 수 체크
        for j in range(n):
            if i&(1<<j):
                total += arr[j]        #arr[j]: 부분집합에 포함된 원소 -> 누적합시킴
                cnt+= 1
        if cnt == N and total == K:
            result+= 1
    print('#{} {}'.format(tc, result))

