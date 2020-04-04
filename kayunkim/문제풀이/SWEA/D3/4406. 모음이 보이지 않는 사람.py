T = int(input())
for tc in range(1,T+1):
    word = input()
    vowel = 'aeiou'
    print('#{} '.format(tc), end='')
    for i in word:
        if i not in vowel:
            print(i, end='')
    print()