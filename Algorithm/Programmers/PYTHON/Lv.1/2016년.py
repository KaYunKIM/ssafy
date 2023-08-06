def solution(a, b):
    answer = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    zero = [4,6,9,11]
    one = [1,3,5,7,8,10,12]
    days = 0
    for i in range(1,a):
        if i in zero:
            days+=30
        elif i in one:
            days+=31
        else:
            days+=29
    days+=b
    return answer[days%7]