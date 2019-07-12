class Trie:

    def __init__(self):
        self.root = Node()

    def add(self, string):

        node = self.root
        for i in range(len(string)):
            if string[i] in node.hash.keys():
                node = node.hash[string[i]] # increment pointer
            else:
                node.hash[string[i]] = Node()
                node = node.hash[string[i]]
        if node.value == False:
            node.value = True


    def is_prefix(self, string):

        node = self.root
        for i in range(len(string)):
            if string[i] in node.hash.keys():
                node = node.hash[string[i]]
            else:
                return False
        return True


    def is_present(self, string):
        node = self.root
        for i in range(len(string)):
            if string[i] in node.hash.keys():
                node = node.hash[string[i]]
            else:
                return False
        if node.value == True:
            return True
        else:
            return False


class Node:

    def __init__(self):
        self.value = False
        self.hash = {}



t = Trie()
t.add('abcd')
print(t.is_prefix('abc'))
print(t.is_present('abc'))
print(t.is_present('abcd'))

t.add('lmn')
print(t.is_present('lmn'))
print(t.is_prefix('lh'))



