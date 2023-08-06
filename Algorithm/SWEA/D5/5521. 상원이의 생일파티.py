def find(cur,start):
    queue = [start]
    # v = set([1])
    v = set([])
    while True:
        temp=[]
        while queue:
            print('q',queue)
            friend = queue.pop(0)
            print(friend,temp)
            for f in friend:
                print('v',v)
                v.add(f)
                temp.append(bin[f])
            print('temp',temp)
        print('temp2',temp)
        queue=temp
        cur+=1
        if cur>2:
            return len(v)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    bin = {i:[] for i in range(N+1)}
    for _ in range(M):
        a,b = map(int,input().split())
        bin[a].append(b)
        bin[b].append(a)
    print(bin)
    if not bin[1]:
        ans = 1
    else:
        ans = find(1,bin[1])
    print('#{} {}'.format(tc,ans-1))