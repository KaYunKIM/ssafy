def perm(k):  #자릿수
    if k == N:
        print(sel)
        return
    for i in range(N):
        if visited[i] ==0:
            sel[k] = arr[i]
            visited[i]=1
            perm(k+1)
            visited[i]=0

arr = [1,2,3]
N = len(arr)
sel = [0]*N
visited = [0]*N
perm(0)