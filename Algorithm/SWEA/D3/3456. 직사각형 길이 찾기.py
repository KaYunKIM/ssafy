T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    if lst[0]!=lst[1]:
        print('#{} {}'.format(tc, lst[0]+lst[1]-lst[2]))
    else:
        print('#{} {}'.format(tc, lst[2]))