def solution(genres, plays):
    answer = []

    temp = {}
    for i in range(len(genres)):
        if genres[i] not in temp:
            temp[genres[i]] = [[plays[i], 0], [i, plays[i]]]

        else:
            temp[genres[i]][0][0] += plays[i]
            temp[genres[i]].append([i, plays[i]])

    order = sorted(temp, key=lambda x: temp[x][0][0], reverse=True)

    for i in order:
        most = sorted(temp[i], key=lambda x: x[1], reverse=True)
        answer.append(most[0][0])
        if most[1][1]:
            answer.append(most[1][0])

    return answer