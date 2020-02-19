age = int(input())

if age >= 20:
    print('adult')
else:
    years = 20-age
    print('{} years later'.format(years))