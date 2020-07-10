cnt = 0
def solution(d, budget):
    if sum(d)<= budget:
        return len(d)
    else:
        visited = [0]*len(d)
        def find(cur,sumV,budget):
            global cnt
            # print(cur,sumV)
            cnt = cur
            if sumV > budget:
                return
            else:
                for i in range(len(d)):
                    if not visited[i]:
                        visited[i]=1
                        find(cur+1,sumV+d[i],budget)
                        visited[i]=0

        find(0,0,budget)
        return cnt
