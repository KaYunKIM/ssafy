def find(start,cnt):
    global N,M
    if cnt == M:
        print(' '.join(start))
        return
    else:
        for i in range(1,N+1):
            find(start+str(i),cnt+1)

N, M = map(int,input().split())
for i in range(1,N+1):
    visited = [0] * (N + 1)
    find(str(i),1)