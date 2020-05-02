T = int(input())
for tc in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))
    bin = {}
    for i in score:
        if i not in bin:
            bin[i]=1
        else:
            bin[i]+=1
    maxV = 0
    for i in bin:
        if bin[i] == max(bin.values()):
            if maxV <= i:
                maxV = i
    print('#{} {}'.format(tc,maxV))