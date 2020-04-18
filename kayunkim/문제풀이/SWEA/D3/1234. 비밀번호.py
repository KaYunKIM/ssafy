T = 10
for tc in range(1,T+1):
    N, pwd = list(input().split())
    ans = pwd[::]
    ans = list(ans)
    h = 0
    while h != int(N):
        for i in range(len(ans)-1):
            if pwd[i] == pwd[i+1]:
                ans.pop(i)
                ans.pop(i)
                print(ans)
        break
        h+=1