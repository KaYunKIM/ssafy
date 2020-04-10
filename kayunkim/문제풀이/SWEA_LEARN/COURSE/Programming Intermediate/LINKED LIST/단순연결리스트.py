class Node:
    def __init__(self, d=0, n=None):
        self.data = d   #data
        self.next = n   #다음 요소 주소

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

#연결리스트 객체 생성 -> 객체의 주소 -> mylist 변수에 담음
mylist= LinkedList()


#출력하기
def printList(lst):
    cur = lst.head
    print(cur.data)

    # cur = cur.next
    # print(cur.data)
    #
    # cur = cur.next
    # print(cur.data)


    print(lst.size, '[', end=' ')
    while cur is not None:
        print(cur.data, end =' ')
        cur = cur.next
    print(']')

#리스트 마지막에 추가하기
def insertLast(lst,new):
#     #빈 리스트일 경우
#     if lst.head is None:   # 빈리스트일 경우
#         lst.head = new
#     else:
#         cur = lst.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = new
#     lst.size +=1

#각 노드 생성
# n5 = Node(5)
# n4 = Node(4,n5)
# n3 = Node(3,n4)
# n2 = Node(2,n3)
# n1 = Node(1,n2)
#
# mylist.head = n1
# mylist.size = 5

#리스트 마지막에 추가하기: tail적용
def insertLast2(lst,new):
    #빈 리스트일 경우
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new
    lst.size+=1


printList(mylist)

for i in range(5):
    insertLast(mylist,Node(i))
    printList(mylist)