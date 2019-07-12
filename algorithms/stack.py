class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

s = Stack()
s.push(10)
s.push(100)
print(s.pop())
print(s.pop())
print(s.pop())
