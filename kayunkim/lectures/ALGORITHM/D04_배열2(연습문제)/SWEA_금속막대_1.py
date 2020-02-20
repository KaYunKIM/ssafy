T= int(input())

for tc in range(1, T+1):
    N = int(input())
    bolts = list(map(str,input().split()))
    sets= []

    for i in range(N):
        if bolts.count(bolts[i*2]) == 1:
            sets.append(bolts.pop(i*2))
            sets.append(bolts.pop(i*2))
            break

    while len(bolts) != 0:
        for i in range(N):
            if bolts[i*2]== sets[-1]:
                sets.append(bolts.pop(i*2))
                sets.append(bolts.pop(i * 2))
                break

    print('#{} {}'.format(tc, ' '.join(sets)))