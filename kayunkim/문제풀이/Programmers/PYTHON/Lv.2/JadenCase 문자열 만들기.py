def solution(s):
    answer = ''
    s = s.split(' ')
    for word in s:
        if word:
            word = list(word)
            if word[0].isalpha():
                word[0] = word[0].upper()
            for k in range(1,len(word)):
                if word[k].isupper():
                    word[k] = word[k].lower()
            answer+=''.join(word)+' '
        else:
            answer+=' '
    return answer[:-1]