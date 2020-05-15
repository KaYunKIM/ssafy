def tree(parent,sum):
    global cnt
    cnt+=1
    if parent not in p:
        return
    else:
        for i in range(len(p)):
            if p[i]==parent:
                tree(c[i],sum+1)

T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())
    node = list(map(int,input().split()))
    p = []
    c = []
    for i in range(len(node)):
        if i%2==0:
            p.append(node[i])
        else:
            c.append(node[i])
    cnt = 0
    tree(N,1)
    print('#{} {}'.format(tc,cnt))