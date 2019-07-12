class LinkedList:

    def __init__(self, node):
        self.data = node.data
        self.head = node
        self.tail = node


    def prepend(self, node):
        node.next = self.head
        self.head = node


    def append(self, node):
        self.tail.next = node
        self.tail = node


    def delete_value(self, value):
        pointer = self.head
        if pointer.data == value:
            self.head = pointer.next

        while pointer.next:
            if pointer.next.data == value:
                pointer.next = pointer.next.next
            pointer = pointer.next



    def pp_print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self,node):
        self.next = node


n1 = Node(10)
n2 = Node(11)
n3 = Node(13)
n4 = Node(5)
# n1.set_next(n2)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.prepend(n4)
# ll.prepend(n2)
ll.pp_print()

ll.delete_value(11)
ll.pp_print()



