##완전탐색(dfs)
di = [0,1]
dj = [1,0]

def find(x,y):
    cnt = mtx[0][0]
    min = 1000000
    stack = [(x,y,cnt)]
    while stack:
        # print(stack)
        i,j,num = stack.pop()
        if (i,j) == (N-1,N-1):
            if num < min:
                min = num
        else:
            for d in range(2):
                ni = i+di[d]
                nj = j+dj[d]

                if 0<=ni<N and 0<=nj<N:
                    # print(min)
                    if num+mtx[ni][nj]< min:
                        stack.append((ni,nj,num+mtx[ni][nj]))
                    else:
                        pass
    return min

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(N)]
    print('#{} {}'.format(tc,find(0,0)))

## 재귀활용
di=[0,1]
dj=[1,0]

def find(i,j,sum):
    global minV
    if (i,j) == (N-1,N-1):
        if sum < minV:
            minV = sum
        return
    else:
        if sum> minV:
            return
        else:
            for d in range(2):
                newi = i+di[d]
                newj = j+dj[d]

                if 0<=newi<N and 0<=newj<N and v[newi][newj]==0:
                    v[newi][newj]=1
                    find(newi,newj,sum+board[newi][newj])
                    v[newi][newj]=0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    minV = 1000000
    v=[[0]*N for _ in range(N)]
    find(0,0,board[0][0])
    print('#{} {}'.format(tc,minV))