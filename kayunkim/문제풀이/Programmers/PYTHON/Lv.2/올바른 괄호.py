def solution(s):
    bin = []
    for i in s:
        if not bin and i==')':
            return False
        if i=='(':
            bin.append(i)
        else:
            if bin[-1]== '(':
                bin.pop()
    if bin:
        return False
    return True