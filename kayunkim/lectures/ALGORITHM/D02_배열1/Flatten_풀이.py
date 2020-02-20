T = 10
M = 100

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        min = 100000     #가장 낮은 수를 찾아야해서
        max = 0         #최대, 최소값 저장
        minidx = 0      #그때의 위치정보 저장
        maxidx = 0
        for j in range(M):
            if max < arr[j]:
                max = arr[j]   #최고 상자높이 갱신
                maxidx = j     #최고 상자높이의 위치 갱신
            if min > arr[j]:
                min = arr[j]
                minidx = j
        #덤핑하기
        arr[maxidx] -= 1        #최대는 하나빼고
        arr[minidx] += 1        #최소는 하나 늘리고

    #덥핑작업 종료 후, 최대 최소값 구하기
    max = 0
    min = 100000
    for i in range(M):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]
    D = max - min
    print('#{} {}'.format(tc, D))