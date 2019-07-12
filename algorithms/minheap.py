class MinHeap:


    def __init__(self):
        # self.head = None
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self.heapify_up()

    def pop(self):
        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return value

    def _get_parent(self, index):
        return (index-2)//2

    def _get_child(self, index):
        return index*2+1, index*2+2


    def heapify_up(self):
        pointer = len(self.heap)-1
        parent = self._get_parent(pointer)
        while parent >= 0 and self.heap[pointer] < self.heap[parent]:
            self.heap[pointer], self.heap[parent] = self.heap[parent], self.heap[pointer]
            pointer = parent
            parent = self._get_parent(pointer)


    def heapify_down(self):
        pointer = 0
        left, right = self._get_child(pointer)

        while left < len(self.heap):

            if right < len(self.heap) and self.heap[left] > self.heap[right]:
                smaller = right
            else:
                smaller = left

            if self.heap[pointer] > self.heap[smaller]:
                self.heap[pointer], self.heap[smaller] = self.heap[smaller], self.heap[pointer]
                pointer = smaller
                left,right = self._get_child(pointer)


    def pprint(self):
        return self.heap

class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


mh = MinHeap()
mh.add(10)
mh.add(12)
mh.add(17)
mh.add(14)
mh.add(11)
mh.add(13)
mh.add(6)

print(mh.pop())

print(mh.pprint())









