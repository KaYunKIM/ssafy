def solution(number, k):
    number = list(number)
    max = 0
    min = 0
    cur = 0
    start = 0
    while len(number) != len(number) - k:
        if int(number[cur]) > max:
            max = int(number[cur])
            # elif number[cur] < min:
            #     min = number[cur]
            # elif number[cur] > min:
            for _ in range(start, cur):
                number.pop(0)
            max = 0
            min = 0
            cur = 0
        elif min < int(number[cur]) < max:
            start = cur
            min = int(number[cur])
            max = min + 1
        cur += 1
    return number

    # answer = ''
    # idx = 0
    # while len(answer)!= len(number)-k:
    #     cur = 0
    #     while idx!= k+len(answer)+1:
    #         # print('f',idx, cur, k+len(answer), 'ans',answer)
    #         if int(cur) < int(number[idx]):
    #             cur, curidx = number[idx], idx
    #         idx+=1
    #     if curidx != k+len(answer):
    #         answer+=number[curidx]
    #         curidx+=1
    #         idx = curidx
    #     else:
    #         answer+=number[curidx:]
    #         break
    # return answer