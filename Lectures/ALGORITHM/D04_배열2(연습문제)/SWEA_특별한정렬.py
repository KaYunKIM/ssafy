T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))

    for j in range(N):
        for i in range(len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                continue
            else:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    pp = []
    for i in range(10):
        if i%2==0:
            pp.append(numbers.pop(-1))
        else:
            pp.append(numbers.pop(0))

    print('#{}'.format(tc), end=' ')
    for i in pp:
        print(i, end=' ')
    print()