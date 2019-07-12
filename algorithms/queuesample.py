class Queue:

    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) > 0:
            value = self.queue[0]
        else:
            return 'Queue empty'
        self.queue = self.queue[1:]
        return value

    def enqueue(self, value):
        self.queue.append(value)

    def peek(self):
        print(self.queue[0])

    def is_empty(self):
        if len(self.queue) > 0:
            return False
        return True



q = Queue()
q.enqueue(10)
q.enqueue(20)

print(q.dequeue())
q.peek()
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())

print(q.is_empty())