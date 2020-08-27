n = int(input())
switch = list(map(int,input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int,input().split())
    if sex == 1:
        for i in range(num-1,len(switch),num):
            if switch[i]==1:
                switch[i]=0
            else:
                switch[i]=1
        print(1,switch)
    else:
        next=1
        while switch[num-1-next] == switch[num-1+next] and num-1-next>=1:
            next+=1
        print(next, num-1-next,num+next)
        for i in range(num-1-next,num+next):
            if switch[i]==1:
                switch[i]=0
            else:
                switch[i]=1
            print(2,switch)
for i in range(0,len(switch),20):
    print(*switch[i:i+20])