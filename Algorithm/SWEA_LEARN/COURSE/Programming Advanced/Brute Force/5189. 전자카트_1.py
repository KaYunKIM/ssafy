def find(num):
    min = 100000000
    stack = [num]
    bin = []
    while stack:
        cnt = 0
        v = [0] * (N+1)
        print(stack)
        cart = stack.pop()

        if v[cart]==0:
            bin.append(cart) #현재까지 지나온 길 누적값
            v[cart] = 1
        if len(bin) == N:   #끝까지 갔으면,
            bin.append(1)
            for j in range(N):
                if cnt+e[bin[j]-1][bin[j+1]-1] < min:   #현재지점까지 값을 다 더했을 때 최소보다 작다면
                    cnt+= e[bin[j]-1][bin[j+1]-1]     #추가
                else:
                    cnt = min           #아니면 현재 최소값 유지
                    break               #뒤에 숫자들은 더해주지 않아도 됨
                print('cnt:{}'.format(cnt))
            if cnt < min:   #최소값 바꿔주기
                min = cnt
            else:
                cnt = min
            print('min:{}'.format(min))
            bin = [1]
        else:       #아직 지나가는 과정이라면
            for i in range(2, N+1):
                print('bin:{}'.format(bin))
                if i not in bin:      #지나가는 길을 하나씩 더해주기
                    stack.append(i)

    return min


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e= [list(map(int,input().split())) for _ in range(N)]
    print('#{} {}'.format(tc,find(1)))

#N=10에 대한 처리 해줄 것!!