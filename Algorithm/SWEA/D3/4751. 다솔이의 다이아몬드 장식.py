T = int(input())
for tc in range(1,T+1):
    word = input()
    bin1 = ['.']
    bin2 = ['.']
    bin3 = ['#']
    for i in range(len(word)):
        bin1.append('.#..')
        bin2.append('#.#.')
        bin3.append('.')
        bin3.append(word[i])
        bin3.append('.#')
    print(''.join(bin1))
    print(''.join(bin2))
    print(''.join(bin3))
    print(''.join(bin2))
    print(''.join(bin1))


