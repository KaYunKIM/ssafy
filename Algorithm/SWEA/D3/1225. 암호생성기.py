for tc in range(1,11):
    T = int(input())
    num = list(map(int,input().split()))
    cnt = 0
    while num[-1] != 0:
        cnt+=1
        if cnt>= 2:
            pw = num.pop(0)
            if pw-cnt+1 <= 0:
                num.append(0)
            else:
                num.append(pw-cnt+1)
        if cnt == 6:
            cnt = 0
    print('#{}'.format(tc),end=' ')
    print(' '.join(map(str,num)))