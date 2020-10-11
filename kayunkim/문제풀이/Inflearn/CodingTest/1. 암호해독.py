text = ['   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ']

for i in text:
    ans = i.strip().replace(' ','')
    print(chr(int(ans.replace('+','1').replace('-','0'),2)), end='')