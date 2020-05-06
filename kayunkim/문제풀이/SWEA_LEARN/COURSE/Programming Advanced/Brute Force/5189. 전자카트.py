def find(num):
    cnt = 0
    min = 100000000
    stack = [num]
    bin = ''
    while stack:
        print(stack)
        cart = stack.pop()
        bin = cart
        print(''.format(tc,bin))
        if len(bin) == N-1:
            bin+='1'
            for j in range(N-1):
                print(j,j+1)
                print(bin[j], bin[j+1])
                cnt+= e[int(bin[j])-1][int(bin[j+1])-1]
            if cnt < min:
                min = cnt
        else:
            # if cnt+e[bin[k]][bin[k+1]] > min:
            #     pass
            # else:
            for i in range(2, N+1):
                print(stack, i)
                print('bin:{}'.format(tc,bin))
                if str(i) not in bin:
                    print(bin)
                    stack.append(bin+str(i))
    print(min)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e= [list(map(int,input().split())) for _ in range(N)]
    find('1')
