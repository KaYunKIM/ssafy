from collections import deque

N, M = map(int,input().split())
ans = []

v = [0]*(N+1)
v[0] = -1

line = deque()
temp = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    v[B]+=1
    temp[A].append(B)

for i in range(1,N+1):
    if v[i] == 0:
        line.append(i)

while line:
    student = line.popleft()
    ans.append(student)
    for j in temp[student]:
        v[j] -= 1
        if not v[j]:
            line.append(j)

print(' '.join(map(str,ans)))