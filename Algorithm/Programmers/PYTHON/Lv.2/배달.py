def solution(N, road, K):
    map = {}

    for r in road:
        if r[0] not in map:
            map[r[0]] = [[r[1], r[2]]]
        else:
            map[r[0]].append([r[1], r[2]])

        if r[1] not in map:
            map[r[1]] = [[r[0], r[2]]]
        else:
            map[r[1]].append([r[0], r[2]])

    v = [K+1] * (N+1)
    v[1] = 1
    queue = []
    for to, dist in map[1]:
        queue.append([to, dist])

    while queue:
        nxt, sumV = queue.pop(0)
        v[nxt] = sumV

        for to, dist in map[nxt]:
            if sumV + dist <= K and sumV + dist < v[to]:
                queue.append([to, v[nxt] + dist])

    return len(v) - v.count(K+1)

# BFS
def solution(N, road, K):
    answer = [1]

    map = [[] for _ in range(N + 1)]
    for frm, to, dist in road:
        map[frm].append([to, dist])
        map[to].append([frm, dist])

    v = [100000000] * (N + 1)
    v[1] = 0

    queue = [[1, 0]]
    while queue:
        nxt, sumV = queue.pop(0)

        for to, dist in map[nxt]:
            if sumV + dist <= K and sumV + dist < v[to]:
                v[to] = sumV + dist
                if to not in answer:
                    answer.append(to)
                queue.append([to, sumV + dist])

    return len(answer)

# 재귀
def solution(N, road, K):
    map = [[] for _ in range(N+1)]

    for frm, to, dist in road:
        map[frm].append([to, dist])
        map[to].append([frm, dist])

    def find(cur, sumV):
        if cur not in answer:
            answer.append(cur)

        for to, dist in map[cur]:
            if not v[to] and sumV + dist <= K and sumV + dist < new[to]:
                v[to] = 1
                new[to] = sumV + dist
                find(to, sumV + dist)
                v[to] = 0
        return

    # 방문여부 체크
    v = [0] * (N + 1)
    v[1] = 1

    # 최단 거리 체크
    new = [1000000000] * (N + 1)
    new[1] = 0

    answer = [1]
    find(1, 0)

    return len(answer)


# 방문 & 최단 거리 동시 체크
def solution(N, road, K):
    map = [[] for _ in range(N+1)]

    for frm, to, dist in road:
        map[frm].append([to, dist])
        map[to].append([frm, dist])

    def find(cur, sumV):
        if cur not in answer:
            answer.append(cur)

        for to, dist in map[cur]:
            if sumV + dist < v[to] and sumV + dist <= K:
                v[to] = sumV + dist
                find(to, sumV + dist)
        return

    # 방문&최단 거리 체크
    v = [1000000000] * (N + 1)
    v[1] = 0

    answer = [1]
    find(1, 0)

    return len(answer)