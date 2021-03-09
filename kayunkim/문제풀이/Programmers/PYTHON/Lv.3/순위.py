# 1차 시도
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

for i in range(1, n + 1):
    if len(win[i]) + len(lose[i]) == n - 1:
        answer += 1

    return answer


# 시간 단축하기
def solution(n, results):
    answer = 0

    # 선수 수 만큼 빈 값의 딕셔너리 만들기
    win = {x: set() for x in range(1, n + 1)}
    lose = {x: set() for x in range(1, n + 1)}

    # win과 lose에 각각 이기고 진 선수들 저장하기
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)


    for i in range(1, n + 1):
        # 나를 이긴 선수들의 이긴 선수 목록에 내가 이긴 선수들 추가하기
        for winner in lose[i]:
            win[winner].update(win[i])

        # 내가 이긴 선수들의 진 선수 목록에 내가 진 선수들 추가하기
        for loser in win[i]:
            lose[loser].update(lose[i])

        # win과 lose 목록이 정리된 후에 두 목록 선수들을 합한 수가 나를 제외한 n-1이라면,
        # 내 앞 뒤 선수들에 의해 내 순위가 정해진 것이므로 answer+1
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer