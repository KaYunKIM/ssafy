T = int(input())
for tc in range(1,T+1):
    N = int(input())
    farm = [list(map(int,input().split())) for _ in range(N)]
    minV = 999999999
    for a in range(N-1):
        for b in range(N-1):
            one = 0
            two = 0
            three = 0
            for c in range(b+1):
                for d in range(a+1):
                    # print('one: {}'.format(farm[c][d]))
                    one+= farm[c][d]
            for e in range(b+1,N):
                for f in range(a+1):
                    # print('two: {}'.format(farm[e][f]))
                    two+= farm[e][f]
            for g in range(N):
                for h in range(a+1,N):
                    # print('three: {}'.format(farm[g][h]))
                    three+= farm[g][h]
            ans = max(one,two,three)-min(one,two,three)
            if minV> ans:
                minV = ans
    print('#{} {}'.format(tc,minV))