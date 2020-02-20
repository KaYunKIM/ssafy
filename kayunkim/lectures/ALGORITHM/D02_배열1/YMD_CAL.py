T = int(input())

for tc in range(1, T+1):
    N = input()
    Y = N[0:4]
    M = N[4:6]
    D = N[6:]
    Month_31 = [1, 3, 5, 7, 8, 10, 12]

    if 1<= int(M) <=12:
        if int(M) in Month_31:
            if 1<= int(D) <=31:
                print('#{} {}/{}/{}'.format(tc,Y,M,D))
            else:
                print('#{} -1'.format(tc))
        elif int(M) == 2:
           if 1<= int(D) <=28:
               print('#{} {}/{}/{}'.format(tc,Y,M,D))
           else:
               print('#{} -1'.format(tc))
        else:
            if 1<= int(D) <=30:
                print('#{} {}/{}/{}'.format(tc,Y,M,D))
            else:
                print('#{} -1'.format(tc))
    else:
        print('#{} -1'.format(tc))