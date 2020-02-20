T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bolts = list(map(str,input().split()))
    print(bolts)
    sets = []
    for i in range(N):
        if bolts.count(bolts[2*i]) == 1:
            sets.append(bolts.pop(2*i))
            sets.append(bolts.pop(2*i))
            break

    # while len(bolts)!=0:
        for i in range(len(bolts)//2):
            if bolts[2*i] == sets[-1]:
                sets.append(bolts.pop(2*i))
                sets.append(bolts.pop(2*i))
                # break

    print('#{} {}'.format(tc, " ".join(sets)))