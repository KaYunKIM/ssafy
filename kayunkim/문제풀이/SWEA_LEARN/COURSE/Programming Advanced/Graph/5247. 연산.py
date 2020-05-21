from collections import deque

def BFS():
    global s, e, result, tc
    while Q:
        num, cnt = Q.popleft()
        if num == e:
            result = cnt
            return

        for i in range(4):
            num2 = 0
            if i == 0:
                num2 = num + 1
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 1:
                num2 = num - 1
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 2:
                num2 = num*2
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 3:
                num2 = num - 10
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

TC = int(input())
num_lst = [0] * 1000001
for tc in range(1, TC+1):
    s,e = map(int, input().split())
    Q = deque()
    Q.append((s, 0))
    num_lst[s] = tc
    result = 0
    BFS()
    print('#{} {}'.format(tc,result))