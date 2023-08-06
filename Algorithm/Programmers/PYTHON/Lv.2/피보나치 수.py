def solution(n):
    bin = []
    for i in range(n+1):
        if i<=1:
            bin.append(i)
        else:
            bin.append(bin[-1]+bin[-2])
    answer = bin[-1]%1234567
    return answer


def solution(n):
    answer =[0]*(n+1)
    for i in range(n+1):
        if i <=1:
            answer[i]=i
        else:
            answer[i]= answer[i-1]+answer[i-2]
    return answer[n]%1234567
