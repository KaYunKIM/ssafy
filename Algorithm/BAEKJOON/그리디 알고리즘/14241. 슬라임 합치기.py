N = int(input())
slime = list(map(int,input().split()))
ans = 0
while len(slime)>=2:
    x = max(slime)
    slime.pop(slime.index(x))
    y = max(slime)
    slime.pop(slime.index(y))
    slime.append(x+y)
    ans+=x*y
print(ans)