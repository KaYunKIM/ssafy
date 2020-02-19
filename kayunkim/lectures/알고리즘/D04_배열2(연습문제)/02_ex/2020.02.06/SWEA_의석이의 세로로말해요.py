T = int(input())
for tc in range(1,T1):
    arr = [list(input()) for _ in range(5)]
    for row in arr:
        print(row)
    print('#{}'.format(tc),end=' ')
    for i in range(15):
        for j in range(5):
            if i < len(arr[j]) and j < len(arr):
                print(arr[i][j], end=' ')
            print()