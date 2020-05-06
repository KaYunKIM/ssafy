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
                        queue.stack((ni,nj,num+mtx[ni][nj]))
                    else:
                        pass
    return min

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(N)]
    print('#{} {}'.format(tc,find(0,0)))