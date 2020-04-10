class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d   #data
        self.prev= p
        self.next = n   #다음 요소 주소

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


# def addLast(lst,new):
#     if lst.head is None:
#         lst.head = lst.tail = new
#     else:
#         new.prev = lst.tail
#         lst.tail.next = new
#         lst.tail = new
#     lst.size+=1


def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None:      #뒤에
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None:    #앞에
            last.next = lst.head
            lst.head.prev = last
            lst.head =first
        else:   #중간
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size+=1


def printList(lst):
    if lst.head is None:
        return
    cur = lst.head
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print()
    cur = lst.head
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.prev
    print()

mylist= LinkedList()

N, M = list(map(int,input().split()))
for i in range(4):
    arr = list(map(int,input().split()))
    addList(mylist, arr)

printList(mylist)

