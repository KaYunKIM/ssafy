def find():
    s = []
    for i in range(len(str)):
        if len(s) != 0:
            ch = s.pop()
            if str[i] != ch:
                s.append(ch)
                s.append(str[i])
        else:
            s.append(str[i])
    return len(s)

T = int(input())
for tc in range(int(input())):
    str = input()
    print('#{} {}'.format(tc, find()))