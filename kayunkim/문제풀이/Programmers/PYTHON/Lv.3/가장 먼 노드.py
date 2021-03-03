# 시간 초과
def solution(n, edge):
    ans = [n] * (n + 1)
    ans[0], ans[1] = 0, 0
    node = [[] for _ in range(n + 1)]

    def find(cur, sumV):
        for i in node[cur]:
            if sumV + 1 < ans[i]:
                ans[i] = sumV + 1
                find(i, sumV + 1)
            else:
                pass
        return

    for i in edge:
        node[i[0]].append(i[1])
        node[i[1]].append(i[0])

    find(1, 0)
    return ans.count(max(ans))

# BFS
def solution(n, edge):
    ans = [n] * (n + 1)
    ans[0], ans[1] = 0, 0
    node = [[] for _ in range(n + 1)]

    for i in edge:
        node[i[0]].append(i[1])
        node[i[1]].append(i[0])

    v = [0] * (n + 1)
    v[1] = 1
    queue = [1]

    while queue:
        cur = queue[0]
        if not node[cur]:
            queue.pop(0)
        else:
            for i in node[cur]:
                if not v[i]:
                    queue.append(i)
                    ans[i] = ans[cur] + 1
                    v[i] = 1

            node[cur] = []

    return ans.count(max(ans))


