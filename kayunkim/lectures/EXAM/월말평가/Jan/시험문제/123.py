def q3(number):
    ans = True
    number = str(number)
    if len(number) == 2:
        if abs(int(number[0]) - int(number[1])) != 1:
            ans = False

    elif len(number) > 2:
        for i in range(1,len(number)- 1):
        if abs(int(number[i]) - int(number[i - 1])) != 1 or abs(int(number[i]) - int(number[i + 1])) != 1:
            ans = False
    return ans

print(q3(89098))