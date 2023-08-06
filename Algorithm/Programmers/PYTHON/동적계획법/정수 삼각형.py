## 시간초과
maxV = 0
def find(cur, total, sumV, triangle):
    global maxV
    if cur[0] == total-1:
        if sumV > maxV:
            maxV = sumV
            return
    else:
        v = [0]*2
        for i in range(2):
            if not v[i]:
                v[i]=1
                find((cur[0]+1,cur[1]+i), total, sumV+triangle[cur[0]+1][cur[1]+i], triangle)
                v[i]=0

def solution(triangle):
    find((0,0), len(triangle), triangle[0][0], triangle)
    return maxV



def solution(tri):
    for i in range(len(tri)-1):
        temp = [0]*len(tri[i+1])
        
        for j in range(len(tri[i])):
            if tri[i][j]+tri[i+1][j] > temp[j]:
                temp[j] = tri[i][j]+tri[i+1][j]
            if tri[i][j]+tri[i+1][j+1] > temp[j+1]:
                temp[j+1] = tri[i][j]+tri[i+1][j+1]
        tri[i+1] = temp
        
    return max(tri[-1])



## 시간 단축
def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):

            if j == 0:
                triangle[i][j]+=triangle[i-1][j]
            elif j== len(triangle[i])-1:
                triangle[i][j]+= triangle[i-1][j-1]
            else:
                addV = max(triangle[i-1][j-1], triangle[i-1][j])
                triangle[i][j]+=addV
                
    return max(triangle[-1])