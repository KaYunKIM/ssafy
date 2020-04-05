T = int(input())
for tc in range(1,T+1):
    org = list(map(int,input()))
    cnt = 0
    for i in range(len(org)):
        if int(org[i]) == 1:
            bin[i::]=1
        elif int(org[i]) == 0:
            bin[i::] =0
        print(bin)
        cnt += 1
        print(cnt)
    print(cnt)


