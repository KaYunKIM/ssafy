# def find(n,k,sum):
#     minV = 100000000
#     v = [0] * (N+1)
#     if n == N:
#         s+= e[k][0]
#         if sumV < minV:
#             minV = sumV
#         return
#     elif minV <= sumV:
#         return
#     else:
#         for i in range(2, N+1):
#             if v[i]==0:
#                 v[i] = 1
#                 find(n+1,k,sumV+e[][i])
#                 v[i]=0
#         return
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     e= [list(map(int,input().split())) for _ in range(N)]
#     print('#{} {}'.format(tc,find(1,0,0)))



def find(num,cur,sumV):
    global minV
    v = [0]*(N+1)
    if num == N:    # 한 줄기 끝
        sumV += e[cur][0]
        if sumV < minV:
            minV = sumV
        return
    elif minV <= sumV:   # 한 줄기 내려가는 과정 =>
        return              #줄기 종료
    else:    # 한 줄기 내려가는 과정 중에 아직 최소값을 도달하지 못했을 때
        for i in range(1,N):
            if v[i]==0:
                v[i]=1
                find(num+1, i, sumV+e[cur][i])
                print(i)
                v[i]=0
        return


f(1,0,0) =                          f(1,0,0) = f(2,)
    f(2,1,18)                   f(2,1,18) = return
        e[1][2]
        f(3,2,18+55)
            sumV = 18+55+18 = 91
            minV = 91
            v[2] =0

stack = [1,3,2,1]
stack.pop()
줄기 = 함수 f[1,2]
줄기.pop()
f(3) => 처리완료
f(2)



      0 1 2 3 4 5
num = 1,1,2,3,5,8
stack = [1,1,2,5,8]
stack.pop()


def re():
    re(n-1)+re(n-2)

    if n <=2:

re(5) = re(4)+re(3)                           re(5) = 5
    re(4)  = re(3)+re(2)                 re(4) = 3
         re(3) = re(2)+re(1) = 2        re(3) =re(1)+re(2) = 2
            re(2)= 1   re(2) =1
                re(1) = 1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e= [list(map(int,input().split())) for _ in range(N)]
    minV = 10000000000
    find(1,0,0)
    print('#{} {}'.format(tc,minV))

    1
   2 3
   3 2
   1 1
 깊이=N
 1
 [2,3]
 [1,3,2,1]
 [1,2,3,1]