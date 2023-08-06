T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(str,input().split())) for _ in range(N)]

    m90 = [[matrix[x][y] for x in range(N-1,-1,-1)] for y in range(N)]
    m180 = [[m90[x][y] for x in range(N-1,-1,-1)] for y in range(N)]
    m270 = [[m180[x][y] for x in range(N-1,-1,-1)] for y in range(N)]

    print('#{}'.format(tc))
    for i in range(N):
        a90 = m90[i][0:N]
        a180 = m180[i][0:N]
        a270 = m270[i][0:N]
        print(''.join(a90), end =' ')
        print(''.join(a180), end=' ')
        print(''.join(a270), end=' ')
        print()
