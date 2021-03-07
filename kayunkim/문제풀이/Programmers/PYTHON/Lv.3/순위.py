def solution(n, results):
    answer = 0
    temp = []

    graph = {}
    for i in results:
        if i[0] not in graph:
            graph[i[0]] = [i[1]]
        else:
            graph[i[0]].append(i[1])

    for i in graph:
        if graph[i]:
            v = [0] * (n + 1)
            stack = [i]

            while stack:
                cur = stack[-1]
                if cur not in graph or len(graph[cur]) == 0:
                    stack.pop()
                    v[cur] = 1
                    
                else:
                    if not v[graph[cur][0]]:
                        stack.append(graph[cur].pop(0))
                    else:
                        stack.pop()

    return answer