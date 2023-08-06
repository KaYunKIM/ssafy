## 정확성 53.8점
def solution(n, t, m, p):
    answer = '0'
    letter = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    for num in range(t*m):
        temp = ''
        number = num
        while num > 0:
            temp+=str(num%n)
            num//=n

        ## 숫자 10~15만 해당 하는 것이 아니라 나머지가 10~15인 모든 숫자에 대해서 처리 필요!   
        if temp and number<= n and temp in letter:
            answer+=letter[temp]
        else:
            answer+=temp[::-1]
        # print(number, temp, answer)
        
        if len(answer) > t*m:
            return answer[p-1:t*m:m]

def solution(n, t, m, p):
    answer = '0'
    letter = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    for num in range(t*m):
        temp = ''
        number = num

        while num > 0:
            temp+=str(letter[num%n])
            num//=n

        answer+=temp[::-1]
        if len(answer) > t*m:
            return answer[p-1:t*m:m]