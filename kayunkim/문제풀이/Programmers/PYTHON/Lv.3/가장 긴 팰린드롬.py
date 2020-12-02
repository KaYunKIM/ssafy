def solution(s):
    answer = 1
    for i in range(len(s)):
        temp = [s[i]]
        for j in range(i+1,len(s)):
            temp.append(s[j])
            if s[j] == s[i]:
                if len(temp)%2==1:
                    if temp[:len(temp)//2] == temp[-1:len(temp)//2:-1]:
                        if len(temp) > answer:
                            answer = len(temp)
                else:
                    if temp[:len(temp)//2] == temp[-1:len(temp)//2-1:-1]:
                        if len(temp) > answer:
                            answer = len(temp)
    return answer