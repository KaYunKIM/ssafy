def solution(number, k):
    answer = ''
    idx = 0
    while len(answer)!= len(number)-k:
        cur = 0
        while idx!= k+len(answer)+1:
            # print('f',idx, cur, k+len(answer), 'ans',answer)
            if int(cur) < int(number[idx]):
                cur, curidx = number[idx], idx
            idx+=1
        if curidx != k+len(answer):
            answer+=number[curidx]
            curidx+=1
            idx = curidx
        else:
            answer+=number[curidx:]
            break
    return answer