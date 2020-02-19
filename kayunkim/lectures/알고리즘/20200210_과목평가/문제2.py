T = int(input())
for tc in range(1,T+1):
    R,C,N = list(map(int,input().split()))
    matrix = [list(map(int,input().split())) for _ in range(N)]

    bin = []
    for i in range(len(matrix)):
        x1 = matrix[i][0]-1
        y1 = matrix[i][1]-1
        x2 = matrix[i][2]-1
        y2 = matrix[i][3]-1

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lst = [x,y]
                bin.append(lst)
    bin_1 = []
    for j in range(R):
        for k in range(C):
            a = bin.count([j,k])
            bin_1.append(a)
    max =0
    for i in bin_1:
        if max < i:
            max = i
    print('#{} {}'.format(tc, bin_1.count(max)))

        # sum = 0
        # for j in range(len(bin)):
        #     print(bin[j])
        # for k in bin[j]:
        #     print(k)
        #     print(bin[j][k])
            # print(bin[j+1][k])
            # for k in bin[j]:
            #     print(k)
            #     print(bin[j+1])
            # print(bin[j+1][0],bin[j+1][1])
                # sum+=1
                # print(sum)
