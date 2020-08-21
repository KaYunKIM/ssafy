def solution(s):
    ans = ''
    temp = ''
    for i in range(len(s)):
        temp+=s[i]
        # for j in range(i+1,len(s)):
        if temp not in s[i+1:len(s)]:
            print(temp)
            ans+=str(len(temp))
            ans+=temp
            temp = ''
    print(ans)
    return len(ans)