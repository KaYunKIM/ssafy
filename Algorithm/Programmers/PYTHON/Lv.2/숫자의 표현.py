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


# 테스트 1 〉	통과 (7.55ms, 10.7MB)
# 테스트 2 〉	통과 (4.41ms, 10.7MB)
# 테스트 3 〉	통과 (5.07ms, 10.7MB)
# 테스트 4 〉	통과 (4.98ms, 10.6MB)
# 테스트 5 〉	통과 (5.77ms, 10.6MB)
# 테스트 6 〉	통과 (5.68ms, 10.7MB)


def solution(n):
    cnt=0
    cur=1
    while cur != n:
        temp=0
        for i in range(cur,n//2+2):
            if temp+i<=n:
                temp+=i
                if temp==n:
                    cnt+=1
                    break
            else:
                break
        cur+=1
    return cnt+1