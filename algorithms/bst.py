from pdb import set_trace as bp
from node import Node


class BinarySearchTree:


    def __init__(self):
        self.root = None
        self.sorted = []
        


    def insert(self, node, root=None):
        if self.root is None:
            self.root = node
            return 

        if root is None:
            root = self.root
        if root.value < node.value:
            if root.right:
                self.insert(node, root.right)
            else:
                root.right = node


        if root.value > node.value:
            if root.left:
                self.insert(node, root.left)
            else:
                root.left = node


    def contains(self, value, root=None):
        
        if root.value == value:
            return True

        if root.value < value:
            if root.right:
                self.contains(value, root.right)
            else:
                return False

        if root.value > value:
            if root.left:
                self.contains(value, root.left)
            else:
                return False

    # def pprint(self):

    #     result = []
    #     to_visit = []
    #     to_visit.append(self.root)


    #     while len(to_visit) > 0:
    #         node = to_visit[0]
    #         # bp()
    #         to_visit = to_visit[1:]
    #         if node:
    #             if node.left:
    #                 to_visit.append(node.left)
    #             if node.right:
    #                 to_visit.append(node.right)
                
    #             # result.append(node.value)
    #             print(node.value)
    #         # result.append(-1)
    #     print(result)

    def preorder(self, root=None):
        if root is None:
            root = self.root
        print(root.value)
        if root.left:
            self.preorder(root.left)
        print('...')
        if root.right:
            self.preorder(root.right)
        print('--')


    def postorder(self, root=None):
        if root is None:
            root = self.root
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)

        print(root.value)

    def inorder(self, root = None):
        if root is None:
            root = self.root

        if root.left:
            self.inorder(root.left)
        print(root.value)
        if root.right:
            self.inorder(root.right)


    def get_sorted(self, root = None):

        if root is None:
            root = self.root

        if root.left:
            self.get_sorted(root.left)

        self.sorted.append(root)

        if root.right:
            self.get_sorted(root.right)


    def _balance(self, _sorted):

        n = len(_sorted)
        if n == 1:
            return
        mid = n // 2
        node = _sorted[mid]

        node.left = self._balance(_sorted[:mid])
        node.right = self._balance(_sorted[mid:])

        return node

    def balance(self, root = None):
        self.get_sorted(self.root)
        print([node.value for node in self.sorted])
        self.root = self._balance(self.sorted)






bst = BinarySearchTree()
n10 = Node(10)
n12 = Node(12)
n17 = Node(17)
n14 = Node(14)
n11 = Node(11)
n13 = Node(13)
n6 = Node(6)



bst.insert(n14)
bst.insert(n12)
bst.insert(n17)
bst.insert(n10)
bst.insert(n11)
bst.insert(n13)
bst.insert(n6)

# bst.pprint()

bst.preorder()

print('\n\n\n\n')
bst.postorder()

print('\n\n\n\n')
bst.inorder()



bst.balance()
print('\n\n\n\n')
bst.preorder()
print('\n\n\n\n')
bst.postorder()




