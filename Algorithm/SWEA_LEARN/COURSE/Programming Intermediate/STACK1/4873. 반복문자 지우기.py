T = int(input())
for tc in range(1,T+1):
    lst = input()
    bin = []
    for i in lst:
        if i not in bin:
            bin.append(i)
        else:
            if i == bin[-1]:
                bin.pop()
            else:
                bin.append(i)
    print('#{} {}'.format(tc,len(bin)))