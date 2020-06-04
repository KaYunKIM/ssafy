def find(cur,start):
    global cnt
    queue = [start]
    print(queue)
    v=[1]
    while queue:
        friend = queue.pop(0)
        temp=[]
        for f in friend:
            if f not in v:
                v.append(f)
                temp.append(bin[f])
                cnt+=1
        print('temp',temp)
        queue=temp
        cur+=1
        if cur>3:
            return v

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    bin = {i:[] for i in range(N+1)}
    for _ in range(M):
        a,b = map(int,input().split())
        bin[a].append(b)
        bin[b].append(a)
    print(bin)
    cnt = 0
    find(1,bin[1])
    print('#{} {}'.format(tc,cnt))