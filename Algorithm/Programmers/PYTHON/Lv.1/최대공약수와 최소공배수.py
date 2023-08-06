def solution(n, m):
    answer = []
    n,m = min(n,m), max(n,m)
    for i in range(1,n+1):
        if m%i ==0 and n%i==0:
            first = i
    answer.append(first)
    for i in range(1,n+1):
        if (m*i)%n == 0:
            last = m*i
            break
    answer.append(last)
    return answer