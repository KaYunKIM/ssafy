def solution(routes):
    answer = 0
    v = [0]*len(routes)
    routes.sort(key=lambda x:x[1])
    camera = -30000
    for i in range(len(routes)):
        if not v[i]:
            camera = routes[i][1]
            for j in range(i,len(routes)):
                if not v[j]:
                    if routes[j][0] <= camera and camera <= routes[j][1]:
                        v[j] = 1
            answer+=1
    return answer