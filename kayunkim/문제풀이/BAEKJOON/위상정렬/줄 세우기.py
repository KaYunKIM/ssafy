from collections import deque

N, M = map(int,input().split())
ans = []

for _ in range(M):
    A,B = map(int,input().split())


print(' '.join(map(str,ans)))