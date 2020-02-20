T = int(input())
for tc in range(1, T + 1):
    N = input().split()
    lst = list(map(str, input().split()))
    num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    for i in range(len(lst)):
        lst[i] = num[lst[i]]
    print(lst)

    bin = []
    for x in range(0, 10):
        a = lst.count(x)
        bin.append(a)
    print(bin)

    result_bin = []
    for y in range(len(bin)):
        for a in num:
            if y == num[a]:
                result = (a+' ') * bin[y]
                print(result, end='')
    #             result_bin.append(result)
    #
    # R = ''.join(result_bin)
    # print('#{}'.format(tc))
    # for i in range(0, len(R) + 1, 3):
    #     print(R[i:i + 3], end=' ')
