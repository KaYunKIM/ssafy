def preorder(start):
    global cnt
    if start:
        preorder(array[start][0])
        preorder(array[start][1])
        cnt += 1

T = int(input())
for tc in range(1,T+1):
    E,N = list(map(int, input().split()))
    array = [[0 for _ in range(2)] for __ in range(E+2)]
    lst = list(map(int, input().split()))
    for idx in range(0, len(lst), 2):
        if array[lst[idx]][0]:
            array[lst[idx]][1] = lst[idx+1]
        else:
            array[lst[idx]][0] = lst[idx+1]
    cnt = 0
    preorder(N)
    print('#{} {}'.format(tc,cnt))