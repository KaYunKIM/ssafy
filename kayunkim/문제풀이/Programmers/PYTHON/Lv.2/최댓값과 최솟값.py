def solution(s):
    answer = ''
    bin = []
    temp = ''
    for i in range(len(s)):
        temp+=s[i]
        print(temp)
        if s[i]==' ':
            bin.append(int(temp))
            temp = ''
    bin.append(int(temp))
    answer+=str(min(bin))
    answer+=' '
    answer+=str(max(bin))
    return answer