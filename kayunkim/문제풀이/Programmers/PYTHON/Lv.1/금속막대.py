tc = int(input())
for tc in range(1,tc+1):
    N = int(input())
    bolts = list(map(int,input().split()))
    bin = []
    i = 0
    while bolts:
        print(i, bolts[i])
        if bolts.count(bolts[i])==1:
            bin.append(bolts[i])
            bin.append(bolts[i+1])
            print(bolts, i)
            bolts.remove(bolts[i])
            print(bolts, i , bolts[i])
            bolts.remove(bolts[i])
            print(bolts,i, bin)
        else:
            i+=2
    return 


