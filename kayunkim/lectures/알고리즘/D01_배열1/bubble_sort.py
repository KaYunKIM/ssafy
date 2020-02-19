bubble = list(map(int,input().split()))
print(bubble)
temp=[]
for i in range(len(bubble)):
    if len(i)> len(i+1):
        temp = len(i)
        len(i) = len(i+1)
        len(i+1) = temp
    else:
        len(i) = len(i)
        len(i+1) = len(i+1)
    print()

def BubbleSort(a):
    for_i in range(len(a)-1,0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1, aj[i]]

arr = [3,4,2,1,5]
BubbleSort(arr)
print(arr)
a= 5
b=1
print(a,b)
b, a = a, b
print(a,b)

