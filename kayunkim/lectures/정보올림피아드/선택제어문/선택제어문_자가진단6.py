sex, age = input().split()


if sex == 'M':
    if int(age) >= 18:
        print('MAN')
    else:
        print('BOY')
else:
    if int(age) >= 18:
        print('WOMAN')
    else:
        print('GIRL')