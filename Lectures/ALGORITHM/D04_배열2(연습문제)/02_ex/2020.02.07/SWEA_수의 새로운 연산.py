grid = [[]]

d = 1       #대각선의 길이

x = 1
y = 2
m = 1

while m <= 10000:
    for x in range(1,d+1):
        y = d - x+1
        grid.append([x,y])
        m+1
    d+= 1
print(grid)

T = int(input())
for tc in range(1, T+1):
    p,q = map(int,input().split())
    # 1 star 5 = #($(1) + &(5))
    # &(1) => (1,1)       &(5) => (2,2)
    # #(1,1) + #(2,2)   = #(3,3)
    x = grid[p][0] + grid[q][0]
    y = grid[p][1] + grid[q][1]
    # #(3,3) -> 13
    n = (x+y-1)*(x+y)//2 -y +1
    print('#{} {}'.format(tc, n))

