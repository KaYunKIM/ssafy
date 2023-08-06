def solution(s):
    s = list(s)
    h = -1
    for i in range(len(s)):
        if not s[i].isalpha():
            h=1
        if h == -1:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
        h*=-1
    return ''.join(map(str,s))