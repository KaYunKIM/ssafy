def find(start,cnt):
    global N,M
    if cnt == M:
        print(' '.join(start))
        return
    else:
        for i in range(int(start[-1])+1,N+1):
            if not visited[i]:
                visited[i] = 1
                find(start+str(i),cnt+1)
                visited[i]=0

N, M = map(int,input().split())
for i in range(1,N+1):
    visited = [0] * (N + 1)
    find(str(i),1)