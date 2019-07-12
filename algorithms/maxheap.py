class MaxHeap:


    def __init__(self):
        # self.head = None
        self.head = None
        self.tail = None


    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        if self.head.left is None:
            self.head.left = node
            self.tail = node
            return
        elif self.head.right is None:
            self.head.right = node
            self.tail = node
            return 

        if self.tail == self.tail.parent.left:
            self.tail.parent.right = node
            self.tail.next = node
        else:
            if self.tail.parent.next:
                self.tail.parent.next.left = node

            else:
                pointer = self.head()
                while pointer.left:
                    pointer = pointer.left
                pointer.left = node

        sef.tail = node
        self.heapify_up()

    def pop(self):
        value = self.head.value
        self.head.value = self.tail.value
        if self.tail.parent.right:
            self.tail = self.tail.parent.left
        else:
            self.tail = self.tail.parent
        self.heapify_down()
        return value


    def heapify_up(self):
        pointer = self.tail
        while pointer.parent and pointer.value > pointer.parent.value:
            pointer.value, pointer.parent.value = pointer.parent.value, pointer.value
            pointer = pointer.parent


    def heapify_down(self):
        pointer = self.head
        left, right = pointer.left, pointer.right

        while left:

            if right and right.value > left.value:
                larger = right
            else:
                larger = left

            if pointer.value > larger.value:
                pointer.value, larger.value = larger.value, pointer.value
                pointer = larger
                left, right = pointer.left, pointer.right


    def pprint(self):
        node = self.head
        result = []
        while node:
            result.append(node.value)
            while node.left:
                result.append(node.left.value)
                node = node.left
                while node.next:
                    result.append(node.next.value)
                    node = node.next
                node = node.parent.parent.left.left




class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.next = None
        self.right = None
        self.left = None


mh = MaxHeap()
n10 = Node(10)
n12 = Node(12)
n17 = Node(17)
n14 = Node(14)
n11 = Node(11)
n13 = Node(13)
n6 = Node(6)

mh.add(n10)


print(mh.pprint())
mh.add(n12)
mh.add(n17)
mh.add(n14)
mh.add(n11)
mh.add(n13)
mh.add(n6)

print(mh.pop())











