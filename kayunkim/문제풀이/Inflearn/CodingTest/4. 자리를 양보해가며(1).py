page = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']
chairs = []
v = []
minute = 0
second = 0
for i in range(len(page)):
    if len(chairs) <3:
        if page[i] in chairs:
            v.append(v.pop(v.index(page[i])))       #[어, 척]
            second += 1
        else:
            chairs.append(page[i])   #[척, 어, 무]
            v.append(page[i])       #[어,척,무]
            minute+=1
    else:
        if page[i] in chairs:
            v.append(v.pop(v.index(page[i])))
            second += 1
        else:
            chairs.pop(chairs.index(v[0]))    #[척, 어, 무]
            chairs.append(page[i])            #[척, 무, 파]
            v.pop(0)                        #[척,무]
            v.append(page[i])               #[척,무,파]
            minute+=1

print('{}분 {}초'.format(minute, second))