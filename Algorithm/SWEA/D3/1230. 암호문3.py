T = 10
for tc in range(1,T+1):
    N1 = int(input())
    original = list(map(int,input().split()))
    N2 = int(input())
    order = list(input().split())
    for i in range(len(order)):
        if order[i] == 'I':
            index = int(order[i+1])
            num = int(order[i+2])
            for j in range(num):
                original.insert(index+j, int(order[i+3+j]))
        elif order[i] == 'D':
            del original[int(order[i+1])-1:int(order[i+1])+int(order[i+2])-1]
        elif order[i] == 'A':
            for j in range(int(order[i+1])):
                original.append(int(order[i+2+j]))
    print('#{}'.format(tc), end =' ')
    for k in range(10):
        print(original[k], end =' ')
    print()