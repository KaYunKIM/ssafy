numbers = input()
temp = ''
ans = 0
cur = '+'
for i in numbers:
    if i == '+' or i == '-':
        if cur == '+':
            ans += int(temp)
        else:
            ans -= int(temp)
        temp = ''
        if i == '-':
            cur = '-'
    else:
        temp += i

if cur == '+':
    ans += int(temp)
else:
    ans -= int(temp)
print(ans)