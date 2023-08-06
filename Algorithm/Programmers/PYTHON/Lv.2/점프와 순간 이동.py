## 효율성 실패
def solution(N):
    num = {}
    num[1] = 1
    v = {}
    queue = [1]
    while N not in num:
        temp = []
        cur = queue.pop(0)
        v[cur] = 1

        if cur+1 not in num:
            num[cur+1] = num[cur]+1
            temp.append(cur+1)
        else:
            if num[cur]+1 < num[cur+1]:
                num[cur+1] = num[cur]+1
                temp.append(cur+1)
                
        if cur*2 not in num:
            num[cur*2] = num[cur]
            temp.append(cur*2)
        else:
            if num[cur] < num[cur*2]:
                num[cur*2] = num[cur]
                temp.append(cur*2)
                
        for i in temp:
            if i not in v:
                queue.append(i)
    return num[N]


def solution(N):
    ans = 0
    while N>0:
        if N%2 == 0:
            N//=2
        else:
            N-=1
            ans+=1
    return ans