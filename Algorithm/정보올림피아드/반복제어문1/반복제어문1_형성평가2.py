lst = list(map(int,input().split()))

i=0
even = 0
odd = 0
while i < len(lst)-1:
    if lst[i]%2==1 :
        odd+=1
    else:
        even+= 1
        if lst[i]== 0:
            break
    i+= 1
print('odd : {}\neven : {}' .format(odd,even))

