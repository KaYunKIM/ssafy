def solution(n):
    cnt=0
    cur=1
    while cur != n+1:
        temp=0
        for i in range(cur,n+1):
            if temp+i<=n:
                temp+=i
                if temp==n:
                    cnt+=1
                    break
            else:
                break
        cur+=1
    return cnt