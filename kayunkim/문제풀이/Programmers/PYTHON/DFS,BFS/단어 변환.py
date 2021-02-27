def solution(begin, target, words):
    answer = 100000000
    v = [0] * len(words)

    def find(cur, target, sumV):
        nonlocal answer
        # print('first',cur, sumV,answer,v)
        if cur == target:
            if sumV < answer:
                answer = sumV
        if sumV > answer:
            return

        for w in range(len(words)):
            if not v[w]:
                cnt = 0
                # print('f',w, words[w])
                for i in range(len(words[w])):
                    if words[w][i] != cur[i]:
                        cnt += 1
                if cnt == 1:
                    # print('s',words[w])
                    v[w] = 1
                    find(words[w], target, sumV + 1)
                    v[w] = 0

    find(begin, target, 0)
    if answer == 100000000:
        return 0
    else:
        return answer