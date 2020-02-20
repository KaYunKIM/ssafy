#앞 뒤 글자 바꾸기
#ABCD

s= list(input())   #['A','B','C','D']
print(s)

'''
A <-> D,  B <-> C

0  1  2  3  <- len(s) -1
['A','B','C','D']
'''

for i in range(0,len(s)//2):    #4//2 -> 2회 -> 0,1
    s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]

for i in range(0,len(s)):
    print(s[i], end ='')
