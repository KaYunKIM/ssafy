N = int(input())
poleA = []
poleB = []
for _ in range(N):
    A,B = map(int,input().split())
    poleA.append(A)
    poleB.append(B)
poleA.sort()
print(poleA, poleB)