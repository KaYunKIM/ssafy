for tc in range(1,11):
    N = int(input())
    matrix = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(len(matrix)):
        for j in range(8-N+1):
            a = matrix[i][j:j+N]

            # i = 0
            # while i < N//2:
            #     if a[k] != a[-k-1]:
            #         break
            #     i+=1
            # if i == N//2:
            #     print(a)

            flag = 0
            for k in range(N//2):
                if a[k] != a[-k-1]:
                    flag = 1
                    break
            if flag == 0:
                cnt+=1

    for i in range(len(matrix)):
        for j in range(8-N+1):
            k = 0
            bin = []
            while k < N:
                b = matrix[j+k][i]
                bin.append(b)
                k += 1
            flag = 0
            for k in range(N//2):
                if bin[k] != bin[-k-1]:
                    flag = 1
                    break

            if flag == 0:
                cnt+=1

    print('#{} {}'.format(tc,cnt))
