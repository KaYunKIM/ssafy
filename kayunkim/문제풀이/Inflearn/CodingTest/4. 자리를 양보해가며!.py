page = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']
chairs = [0]*3
v = [0]*3
minute = 0
second = 0
h = 0
for i in range(len(page)):
    if 0 in chairs:
        if page[i] not in chairs:
            chairs[h] = page[i]
            v[h] = i+1
            minute+=1
            h+=1
        else:
            v[chairs.index(page[i])] = i+1
            second += 1
    else:
        if page[i] not in chairs:
            clear = v.index(min(v))
            chairs[clear] = page[i]
            v[clear] = i+1
            minute += 1
        else:
            v[chairs.index(page[i])] = i+1
            second += 1
print('{}분 {}초'.format(minute, second))