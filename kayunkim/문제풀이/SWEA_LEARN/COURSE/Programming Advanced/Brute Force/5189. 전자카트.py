def find(num):
    min = 100000000
    stack = [num]
    bin = ''
    while stack:
        cnt = 0
        print(stack)
        cart = stack.pop()
        bin = cart
        if len(bin) == N:
            bin+='1'
            for j in range(N):
                print(bin[j], bin[j+1])
                if cnt+e[int(bin[j])-1][int(bin[j+1])-1] < min:
                    cnt+= e[int(bin[j])-1][int(bin[j+1])-1]
                else:
                    cnt = min
                    break
                print('cnt:{}'.format(cnt))
            if cnt < min:
                min = cnt
            else:
                cnt = min
            print('min:{}'.format(min))
        else:
            for i in range(2, N+1):
                print('bin:{}'.format(bin))
                if str(i) not in bin:
                    stack.append(bin+str(i))
    return min


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e= [list(map(int,input().split())) for _ in range(N)]
    print('#{} {}'.format(tc,find('1')))