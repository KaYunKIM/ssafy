for T in range(int(input())):
    lst = list(input())
    bin = []
    for i in range(len(lst)):
        if lst[i] in bin:
            if lst[i] == bin[-1]:
                bin.pop()
            else:
                bin.append(lst[i])
        else:
            bin.append(lst[i])
    print('#{} {}'.format(T+1,len(bin)))