#방법1
s = 'Reverse this string'
s_rev = ''
for ch in s:        #문자열은 시퀀스형 -> 반복문 적용 가능(한 글자씩 적용)
    print(ch)
    s_rev = ch + s_rev
    print(s_rev)

# #방법2
# s = 'Reverse this string'
# s_list = list(s)
# s_list.reverse()
# print(s_list)
# print(''.join(s_list))
#
# #방법3
# s = 'Reverse this string'
# print(''.join(reversed(s)))
#
# #방법4
# s = 'Reverse this string'
# print(s[:])        #모든 문자열
# print(s[0:3])
# print(s[-1:-len(s)-1:-1])
# print(s[::-1])      #모든 구간에서 거꾸로 돌아간다
