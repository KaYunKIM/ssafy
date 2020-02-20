n,m = map(int,input().split())
lst = []

for i in range(1,n+1):
    for j in range(1,m+1):
        lst.append(i*j)
for x in range(0,len(lst),5):
    print(x)
    print(lst[x:(x+5)])