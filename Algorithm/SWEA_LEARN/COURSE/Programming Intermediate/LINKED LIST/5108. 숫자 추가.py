class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        HeadNode = Node(data)
        self.head = HeadNode       #첫번째 노드 주소
        self.size = 0          #리스트 크기

    def insert(self, idx, data):
        node = self.head
        insertNode = Node(data)
        start = node.next
        start.next = insertNode
        insertNode.next = start
        self.size += 1

def printList(lst):
    cur = lst.head
    while cur.next != None:
        print(cur.next.data)
        cur = cur.next

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    num = list(map(int,input().split()))
    mylist = LinkedList()
    for i in range(M):
        a,b = list(map(int,input().split()))
        mylist.insert(a,b)
    printList(mylist)
