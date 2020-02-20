n = 5
m = 9

W = n*'*'
H = W*m
print(len(H))


for i in range(5):
    print(H[i*5:(i+1)*5])
