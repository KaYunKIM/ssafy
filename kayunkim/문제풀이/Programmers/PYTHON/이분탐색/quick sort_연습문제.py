def find(subject):
    if len(subject)<=1:
        return subject
    last = subject[-1]
    small=[]
    large=[]
    for i in range(0,len(subject)-1):
        if subject[i] <=last:
            small.append(subject[i])
        else:
            large.append(subject[i])
    return find(small)+[last]+find(large)


d = [6,8,3,9,10,1,2,4,7,5]
print(find(d))