def find(cur,cnt):
    global N,M
    if M ==1:
        print(cur)
        return
    else:
        if cnt == M:
            print(' '.join(cur))
            return
        else:
            visited[int(cur[-1])] = 1
            for i in range(1,N+1):
                if not visited[i]:
                    visited[i] = 1
                    find(cur+str(i),cnt+1)
                    visited[i] = 0


N, M = map(int,input().split())
for i in range(1,N+1):
    visited = [0] * (N + 1)
    find(str(i),1)