T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus_no = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = []
    for _ in range(P):
        C = int(input())
        bus_stop.append(C)
    V = [0]*P
    for i in bus_no:
        for j in range(len(bus_stop)):
            if i[0]<= bus_stop[j]<= i[1]:
                V[j]+=1

    print('#{} {}'.format(tc, ' '.join(map(str, V))))
