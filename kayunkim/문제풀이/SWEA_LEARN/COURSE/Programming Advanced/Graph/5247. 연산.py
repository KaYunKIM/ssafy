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




3
2 7
3 15
36 1007

deque(덱)
double-ended queue
앞과 뒤 양방향에서 데이터를 처리할 수 있는 구조
데이터 처리속도가 빠름(이중연결리스트로 구현)

- append(x): 덱의 가장 뒤에 x를 삽입한다.
- appendleft(x): 덱의 가장 앞에 x를 삽입한다.
- pop(): 덱의 가장 마지막 원소를 제거하며 반환한다.
- popleft(): 덱의 가장 처음 원소를 제거하며 반환한다.

'''
from collections import deque
def bfs(n,m):
    v = {n:1}
    # q = [n]
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        t = [n-10,n-1,n+1,n*2]
        for i in range(4):
            if t[i] == m:
                return v[n]
            if t[i] > 0 and t[i] <= 1000000:
                if v.get(t[i]) == None:
                    v[t[i]] = v[n] + 1
                    q.append(t[i])

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    print('#{} {}'.format(tc,bfs(N,M)))
