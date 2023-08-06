T = 10
for tc in range(1,T+1):
    N = int(input())
    pwd = list(map(int,input().split()))
    M = int(input())
    update = list(input().split())
    for i in range(len(update)):
        if update[i] == 'I':
            cnt = int(update[i+2])
            idx = int(update[i + 1])
            while cnt!= 0:
                pwd.insert(idx, update[i+3+int(update[i+2])-cnt])
                cnt-=1
                idx+=1

    print('#{} {}'.format(tc,' '.join(map(str,pwd[:10]))))