T = int(input())

for tc in range(1,T+1):
    lst = list(input())
    s = []
    for i in lst:
        if i == '(':
            s.append(i)
        else:
            while len(s) != 0:
                s.pop()
        print(s)


