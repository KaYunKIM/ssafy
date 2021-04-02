def solution(name):
    answer = 0
    start = list('A' * (len(name) - 1))
    idx = 0
    while True:
        answer += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]))
        start[idx] = name[idx]

        if start == name:
            return answer

        left, right = 1, 1
        for i in range(1, len(name)):
            if name[idx - i] == 'A':
                left += 1
            else:
                break

        for i in range(1, len(name)):
            if name[idx + 1] == 'A':
                right += 1
            else:
                break

        if left > right:
            idx += right
        else:
            idx -= left
        answer += min(left, right)