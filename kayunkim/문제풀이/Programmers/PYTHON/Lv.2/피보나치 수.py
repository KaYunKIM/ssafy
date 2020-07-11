def solution(n):
    bin = []
    for i in range(n+1):
        if i<=1:
            bin.append(i)
        else:
            bin.append(bin[-1]%1234567+bin[-2]%1234567)
    answer = bin[-1]%1234567
    return answer