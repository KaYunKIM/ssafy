def paper(x):
    if x == N:
        return 1
    elif x > N:
        return 0
    else:
        return paper(x + 10) + paper(x + 20) * 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(tc, paper(0)))