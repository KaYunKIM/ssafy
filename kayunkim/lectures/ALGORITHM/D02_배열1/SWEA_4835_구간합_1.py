def find(n,m):
    sum = 0
    for i in range(0,m):         #맨 처음의 0,1,2의 인덱스의 값 더하기
        sum+= v[i]
    minV = sum
    maxV = sum
    for i in range(1, n-m+1):    #나머지 구간에 대해서 누적합 구하기
        sum - v[i-1] + v[i+m-1]  #이미 구해진 구간합에서 앞의 수는 빼고 뒤의 수는 더해줌
        if sum > maxV:
            maxV = sum
        if sum < minV:
            minV = sum
    return maxV - minV

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    v = list(map(int,input().split()))
    print('#{} {}'.format(tc, find(N,M)))
