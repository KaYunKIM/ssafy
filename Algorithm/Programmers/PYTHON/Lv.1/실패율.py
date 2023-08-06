def solution(N, stages):
    bin = {}
    user = len(stages)
    for i in range(1,N+1):
        if stages.count(i) !=0:
            bin[i] = stages.count(i)/user
        else:
            bin[i] = 0
        user-=stages.count(i)
    return sorted(bin, key=lambda x: bin[x], reverse=True)