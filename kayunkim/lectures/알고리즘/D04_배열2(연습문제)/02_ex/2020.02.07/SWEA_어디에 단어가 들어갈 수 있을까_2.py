import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    bin = []
    sum_a = 0
    sum_b = 0

    for i in range(N):
        bin.append(sum_a)
        bin.append(sum_b)
        sum_a = 0
        sum_b = 0
        for j in range(N):
            if matrix[i][j] == 1:
                sum_a+=1
            else:
                bin.append(sum_a)
                sum
        if cnt == K:
            bin[i].append(cnt)
            print(bin[i])
            cnt = 0
            print(bin)
        # print(bin[i].count(3))


            for j in range(N):
                if k[i][j] == 1:
                    suma += 1
                else:
                    sumlist.append(suma)
                    suma = 0

                if k[j][i] == 1:
                    sumb += 1
                else:
                    sumlist.append(sumb)
                    sumb = 0
        sumlist.append(suma)
        sumlist.append(sumb)
        result = sumlist.count(M)
        print('#{} {}'.format(tc, result))


    # print('#{} {}'.format(tc, sum))