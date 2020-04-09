# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self,data):
#         HeadNode = Node(data)
#         self.head = HeadNode       #첫번째 노드 주소
#         self.size = 0          #리스트 크기


def insert(m):
    for _ in range(M):
        idx, val = map(int,input().split())
        num.insert(idx,val)

def printList(lst):
    return num[lst]


T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    num = list(map(int,input().split()))
    insert(M)
    ans = printList(L)
    print('#{} {}'.format(tc, ans))