class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        root.next = None
        node = root
        while node.left:
            leftmost = node
            while node:
                node.left.next = node.right
                node.right.next = node.next.left if node.next else None
                node = node.next
            
            node = leftmost.left
        
        return root


    root.next = None

    node = root.left
    leftmost = root

    while node.left:
        leftmost = node
        while node:
            node.left.next = node.right
            node.right.next = node.next.left if node.next else None
            node = node.next

        node = leftmost.