def solution(s):
    # cntp = 0
    # cnty = 0
    # for i in s:
    #     if i == 'p' or i == 'P':
    #         cntp+=1
    #     elif i == 'y' or i == 'Y':
    #         cnty+=1
    # if cntp!=cnty:
    #     return False
    # return True

    # if s.lower().count('p')!= (s.lower().count('y')):
    #     return False
    # return True

    return s.lower().count('p') == (s.lower().count('y'))