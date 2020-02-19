sum = 0
cnt = 0
while True:
    T = list(map(int,input().split()))
    for i in T:
        sum+= i
        cnt+= 1
    if i >= 100:
        print(sum)
        print(round(sum/cnt,1))