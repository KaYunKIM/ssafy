def bs(num,start,end):
    global cnt
    bin = []
    if num == A[(start+end)//2]:
        if 'l' in bin and 'r' in bin:
            cnt+=1
            return cnt
        else:
            return cnt
    else:
        if A[(start+end)//2] < num:
            bin.append('r')
            bs(num,(start+end)//2+1, end)
        elif A[(start+end)//2] > num:
            bin.append('l')
            bs(num,start,(start+end)//2-1)
        else:
            cnt+=1



T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    cnt = 0
    for i in B:
        if i in A:
            if i == A[N//2]:
                cnt+=1
            else:
                print(bs(i,0,(N-1)), i)
    print("cnt", cnt)
