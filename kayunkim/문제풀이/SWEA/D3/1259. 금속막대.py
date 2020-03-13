T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bolt = list(map(int,input().split()))
    bin = []
    for i in range(0,len(bolt),2):
        cnt = 0
        for j in range(1,len(bolt),2):
            if bolt[i] != bolt[j]:
                cnt+=1
        if cnt == len(bolt)//2 :
            bin.append(bolt[i])
            bin.append(bolt[i+1])
    while len(bin) != len(bolt):
        for i in range(0,len(bolt),2):
            if bin[-1] == bolt[i]:
                bin.append(bolt[i])
                bin.append(bolt[i+1])
    print('#{} {}'.format(tc,' '.join(map(str,bin))))