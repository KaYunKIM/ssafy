T = int(input())
for tc in range(1,T+1):
    cards = input()
    binS = []
    binD = []
    binH = []
    binC = []
    bin = {'S':13, 'D':13, 'H':13, 'C':13}
    ans = bin
    for i in range(0,len(cards),3):
        if cards[i] == 'S':
            if cards[i:i + 3] not in binS:
                binS.append(cards[i:i + 3])
                bin['S']-=1
            else:
                ans = 'ERROR'

        elif cards[i] == 'D':
            if cards[i:i + 3] not in binD:
                binD.append(cards[i:i + 3])
                bin['D']-=1
            else:
                ans = 'ERROR'

        elif cards[i] == 'H':
            if cards[i:i + 3] not in binH:
                binH.append(cards[i:i + 3])
                bin['H']-=1
            else:
                ans = 'ERROR'

        elif cards[i] == 'C':
            if cards[i:i + 3] not in binC:
                binC.append(cards[i:i + 3])
                bin['C']-=1
            else:
                ans = 'ERROR'

    if ans != 'ERROR':
        print('#{} '.format(tc), end='')
        for v in bin.values():
            print('{}'.format(v), end = ' ')
        print()
    else:
        print('#{} {}'.format(tc,ans))