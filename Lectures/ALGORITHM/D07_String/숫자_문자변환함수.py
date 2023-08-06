# str_num = '123'
# print(str_num)
# print(type(str_num))            #type() : 타입확인함수
# num = int(str_num)              #int(): 타입변환함수 : str -> int
# print(num)
# print(type(num))                #type() : 타입확인함수
#
# #실수변환
# print(float('3.14'))                   #float() : 실수형으로
# print(type(float('3.14')))             #float() : 실수형으로
#
# #수를 문자로
# print(str(123))                 #str() : 문자열로
#
# #'a'
# #'0'
# print(ord('a'))  #ord() : 'a' 문자의 코드 값
# print(ord('0'))

def atoi(s):
    for i in range(0, len(s)):
        #print(s[i])
        #print(int(s[i]))
        n = n*10  #0 -> 0, 1-> 10, 2 -> 20
        n = n + int(s[i])
    return n

s= input()
print(type(s))
#숫자로 생긴 문자 -> 숫자로 변경하는 함수
r = atoi(s)        #문자를 입력 받아서 int형으로 변환해서 리턴
print(r)

