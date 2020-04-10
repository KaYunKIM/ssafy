class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d   #data
        self.prev= p
        self.next = n   #다음 요소 주소

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

def addLast(lst,new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1


def printList(lst):
    if lst.head is None:
        return
    cur = lst.head
    for _ in range(lst.size*2):
        cur = cur.next
    cur = lst.head.prev
    for _ in range(lst.size*2):
        print(cur.data, end=' ')
        cur = cur.prev


T = int(input())
for tc in range(1,T+1):
    N,M,K = list(map(int,input().split()))
    arr= list(map(int,input().split()))
    mylist = LinkedList()
    for val in arr:
        addLast(mylist, Node(val))

    cur = mylist.head
    for _ in range(M):
        for _ in range(K):
            cur = cur.next

        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new   #새로 추가된 위치를 시작위치로 재설정
        mylist.size +=1

    # print('#{}'.format(tc))
    printList(mylist)
    print()

