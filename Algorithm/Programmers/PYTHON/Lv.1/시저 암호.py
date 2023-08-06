def solution(s, n):
    s= list(s)
    for i in range(len(s)):
        h = ord(s[i])
        if (65<=h<=90 and h+n >90) or (97<=h<=122 and h+n>122):
            s[i] = chr(h+n-26)
        elif h >= 65:
            s[i] = chr(h+n)
    return ''.join(s)