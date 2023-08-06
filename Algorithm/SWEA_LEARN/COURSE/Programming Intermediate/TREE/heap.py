class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    #삽입하기: 배열의 마지막에 삽입, 합구조를 만들어줌
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)

    #현재노드가 부모노드보다 작으면 자리변경 -> root까지 반복
    def percUp(self,i):
        while i//2>0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2].self.heapList[i]
            i = i//2

    def printHeap(self):
        print(self.heapList)

    def delMin(self):


    def percDown(self,i):
        while i+2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i],slef.heapList[mc] = self.heapList[mc],self.heapList[i]

    hp = BinHeap()
    arr=[34,27,3,50,40]
    for n in arr:
        hp.insert(n)
        hp.printHeap()
