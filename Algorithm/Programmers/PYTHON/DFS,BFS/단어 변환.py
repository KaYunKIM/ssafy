def solution(begin, target, words):
    maxV = len(words)

    def find(cur, sumV):
        nonlocal maxV

        if cur == target:
            if sumV < maxV:
                maxV = sumV
            return

        if sumV > maxV:
            return

        for word in words:
            if not v[words.index(word)]:

                cnt = 0
                for i in range(len(word)):
                    if cur[i] != word[i]:
                        cnt += 1

                if cnt == 1:
                    v[words.index(word)] = 1
                    find(word, sumV + 1)
                    v[words.index(word)] = 0

    if target not in words:
        return 0
    else:
        v = [0] * len(words)
        find(begin, 0)
        return maxV