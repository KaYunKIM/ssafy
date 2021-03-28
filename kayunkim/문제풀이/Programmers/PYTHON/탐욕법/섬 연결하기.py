def solution(n, costs):
    answer = []
    new = [[] for _ in range(n)]

    for x, y, p in costs:
        new[x].append((y, p))
        new[y].append((x, p))

    def find(cur):
        for to, cost in new[cur]:
            if cost < v[to]:
                temp = cost
                v[to] = cost
                find(to)
        return

    v = [10000000] * (n)
    for i in range(len(new)):
        if new[i]:
            find(i)
            v[i] = 0
            break

    return sum(v)