T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    n = 1
    while n != N - 1:
        max = 0
        for i in range(N):
            if max < lst[i]:
                max = lst[i]
            else:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        n += 1

    bin = []
    while len(bin) != 10:
        bin.append(lst.pop())
        bin.append(lst.pop(0))

    print('#{} {}'.format(tc, ' '.join(map(str, bin))))