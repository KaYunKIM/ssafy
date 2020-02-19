#2차원리스트

#2행 4열 2차원 리스트
arr = [[1,2,3,4],[5,6,7,8]]
# print(arr)

#1차원 리스트 초기화
arr = [0,0,0,0,0]
arr = [0]*5
arr = [i for i in range(2,9) if i%2==0]
# print(arr)


#2차원 리스트 초기화
brr = [[1,2,3],[4,5,6],[7,8,9]]
# print(brr)
brr = [[1,2,3,]]*3
# print(brr)
brr = [[1,2,3] for i  in range(3)]    #리스트 내포 이용해서 초기화
# print(brr)
brr = [[i,j] for i in range(3) for j in range(2)]
# print(brr)

#2차원 배열 입력받기
# 3 4
# 0 1 0 0
# 0 0 0 0
# 0 0 1 0


#방법1
# n,m = map(int,input().split())
# mylist = [0 for _ in range(n)]
# for i in range(n):
#     mylist[i] = list(map(int,input().split()))    #한 줄 읽어서 공백으로 구분하고 리스트로 변환
# print(mylist)

#방법2
# n,m = map(int,input().split())
# mylist=[]
# for i in range(n):
#     mylist.append(list(map(int, input().split())))
# print(mylist)

#방법3
# n,m = map(int,input().split())
# mylist = [list(map(int,iput().split())) for _ in range(n)]
# print(mylist)


# #리스트 순회
# #n*m개의 원소를 빠짐없이 조사하는 방법
# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(len(arr))
# print(len(arr[0]))
#
# #행 우선순회
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j], end ='')
#     print()
#
# #열 우선순회
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j], end='')
#     print()
#
#
# #지그재그 순회
# N = len(arr)
# M = len(arr[0])
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j+(M-1-2*j)*(i%2)], end='')
#
# for i in range(N):
#     if i%2==0:
#         for j in range(M):
#             print(arr[i][j], end='')
#     else:
#         for j in range(M-1, -1, -1):
#             print(arr[i][j], end='')

#2차원 리스트에서 원하는 데이터의 위치 찾기
# 3 4
# 0 1 0 0
# 0 0 0 0
# 0 0 1 0

# n,m = map(int,input().split())
# mylist = [list(map(int, input().split())) for _ in range(n)]
# newlist = [[i,j]] for i in range(n) for j in range(m) if mylist[i][j]==1]
# print(newlist)

#전치행렬
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# for row in arr:
#     print(row)
#
# for i in range(3):
#     for j in range(3):
#         if i <j:
#             arr[i][j],arr[j][i] = arr[j][i],arr[i][j]



arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
dx= [-1,0,1,0] #위, 오른쪽, 아래, 왼쪽
dy = [0,1,0,-1]

for x in rangae(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
        if nextX >=0 and nextX < len(arr) and nextY >=0 and nextY < len(arr[0]):
            print(arr[nextX][nextY], end='')
        print()
        #arr[x][y]


#연습문제
2 7 4 3 6
8 5 8 3 2
2 2 3 6 9
5 9 2 5 7
3 6 2 9 4
arr = []
for i in range 5:
    for j in range 5:
        arr[i][j] = abs(arr[i-1][j]) + abs(arr[i][j+1]) + abs(arr[i+1][j]) + abs(arr[i][j-1])


