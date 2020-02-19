#문자열 비교함수
#맞으면 1, 아니면 0 리턴
#hello
#hell

def f(s1,s2):
    i = 0
    while (i< len(s1) and i < len(s2)):     #문자열 길이만큼 반복
        if s1[i] == s2[i]:                  #비교하는 문자가 같다면
            i+=1                            #인덱스 늘려주기
        else:                               #비교하는 문자가 다르다
            break
    if i == len(s1) and i == len(s2):       #문자열 비교를 마쳤을 때 두 문자열의 길이가 같다면
        return 1                            #같음
    else:                                   #길이가 다르다면
        return 0                            #다름

#두 문자열 비교
s1 = input()
s2 = input()

if s1 == s2:       #==연산자를 이용해서 문자열 비교
    print(1)
else:
    print(0)
