def solution(s):
    ans = ''
    minV = 1000000000000
    h = 1
    while h != len(s)//2:
        temp = []
        for i in range(0,len(s),h):
            if not temp:
                temp.append(h)
                temp.append(s[i:i+h])
            else:
                if temp[-1] == s[i:i+h]:
                    temp[-2]+=1
                else:
                    temp.append(h)
                    temp.append(s[i:i+h])
        print(temp)
        while 1 in temp:
            temp.remove(1)
        if len(temp)< minV:
            minV = len(temp)
            print(minV)
        h+=1
    return minV