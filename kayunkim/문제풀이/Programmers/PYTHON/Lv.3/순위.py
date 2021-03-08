def solution(n, results):
    answer = 0

    win = {x: [] for x in range(1, n + 1)}
    lose = {x: [] for x in range(1, n + 1)}

    for winner, loser in results:
        if loser not in win[winner]:
            win[winner].append(loser)
        if winner not in lose[loser]:
            lose[loser].append(winner)

    for i in range(1, n + 1):
        for loser in win[i]:
            for j in lose[i]:
                if j not in lose[loser]:
                    lose[loser].append(j)

        for winner in lose[i]:
            for j in win[i]:
                if j not in win[winner]:
                    win[winner].append(j)

    # print(win)
    # print(lose)
    # print()

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer