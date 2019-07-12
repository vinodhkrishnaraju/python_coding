class Node:

    def __init__(self, data):
        self.data = data
        self.adjacent = []
        self.value = data
        self.left = None
        self.right = None

    def set_adjacent(self, list_of_nodes):
        self.adjacent.extend(list_of_nodes)
