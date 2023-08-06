'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01
'''

T = int(input())

for tc in range(1, T+1):
    #카드 유무를 저장 할 2차원 배열
    deck = [[0 for i in range(13)] for j in range(4)]
    types = ['S','D','H','C']
    cards = list(input())
    isError = False

    while cards and not isError:
        type = cards.pop(0)
        nums = cards.pop(0)
        nums = nums+cards.pop(0)
        nums = int(nums)

        for i in range(len(types)):
            if type == types[i]:
                if deck[i][nums] == 0:   #아직카드가 없다면
                    deck[i][nums] = 1    #1로 채움
                else:
                    isError = True
                    break
    print('#{}'.format(tc),end='')
    if isError:
        print('ERROR')
    else:
        for row in deck:
            need = 0
            for c in row:
                if c == 0:
                    need+=1
            print(need, end='')
        print()
