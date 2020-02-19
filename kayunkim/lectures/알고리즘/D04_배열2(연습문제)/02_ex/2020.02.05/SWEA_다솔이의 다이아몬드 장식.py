T = int(input())

for tc in range(1, T+1):
    letter = list(input())
    n = len(letter)
    lst1 = ['.'] * (4*n+1)
    lst2 = ['.'] * (4 * n + 1)
    lst3 = ['#'] * (2 * n + 1)

    for i in range(2,len(lst1),4):
        lst1[i] = '#'
    # print(''.join(lst1))
    for j in range(1,len(lst2),2):
        lst2[j] = '#'
    # print(lst2)
    for k1 in letter:
        for k in range(1, len(lst3), 2):
            lst3[k] = '.'+k1+'.'
        print(lst3)



    # for i in range(n):
    #     # if i == 1:
    #     #     '#..'*n
    #     #
    #     # else:
    #     #
    #     # '#...'*n
    #     # '#.'*2n
    #     # print('#.'+letter[i]+'.', end ='')
    #     print('#.{}.'.format(letter[i]),end='')
    # print()
