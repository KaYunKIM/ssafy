# Day02_WS

### 1. 

```
n = 5
m = 9

W = n*'*'
H = W*m
print(len(H))


for i in range(5):
    print(H[i*5:(i+1)*5])
```



### 2.

``` odd = []
student = {'python' : 80, 'algorithm' : 99, 'django': 89, 'flask': 83}

sum= 0
for subjects in student.values():
    sum+=subjects
    avg = sum/(len(student))
print(avg)
```



### 3.

```
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

a= {}
for BT in blood_types:
    a[BT] = blood_types.count(BT)
print(a)
```

