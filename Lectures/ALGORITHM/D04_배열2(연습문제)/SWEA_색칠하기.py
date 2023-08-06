T= int(input())

for tc in range(1, T+1):
    N = int(input())
    red = []
    blue = []
    cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    red.append((i,j))
                else:
                    blue.append((i,j))

    for i in range(len(red)):
        red_c = red[i]
        for j in range(len(blue)):
            blue_c = blue[j]
            if red_c == blue_c:
                cnt+= 1
    print('#{} {}'.format(tc,cnt))