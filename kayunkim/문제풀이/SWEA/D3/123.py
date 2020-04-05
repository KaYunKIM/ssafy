a = "000111010011111000"
n = 2
cnt = 0
max = 0

# for i in range(len(a)-1):
#     if a[i] != a[i+1]:
#         cnt+=1
#     print(cnt)

cur = 0
for i in range(cur,len(a)):
    print('cur: {}'.format(cur))
    if a[i] == '0':
        print(a[1])
        print('first i:{}',format(i))
        cnt+=1
        print('c:{}'.format(cnt))
    if cnt == n:
        print(a[cur:i+1])
        # print(len(a[cur:i + 1]))
        print('i: {}'.format(i))
        cur = i
        cnt=0

