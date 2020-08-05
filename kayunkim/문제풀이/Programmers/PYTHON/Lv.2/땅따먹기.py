maxV = 0
temp = -1

def find(cur,sumV,fin,land,v):
    global maxV, temp
    if cur == fin:
        if sumV >maxV:
            maxV = sumV
            return
    else:
        for i in range(4):
            if not v[i] and i!=temp:
                v[i]=1
                temp = i
                find(cur+1,sumV+land[cur][i],fin,land,v)
                print(cur, i)
                print(sumV, land[cur][i], sumV+land[cur][i], temp)
                v[i]=0

def solution(land):
    v = [0]*4
    ans = find(0,0,len(land),land,v)
    return maxV

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))