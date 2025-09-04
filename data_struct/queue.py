class MyQueue:
    def __init__(self, capacity):
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0
    def enqueue(self, element):
        if (self.rear+1)%len(self.list) == self.front:
            raise Exception()
        self.list[self.rear] = element
        self.rear = (self.rear+1)%len(self.list)
    def dequeue(self):
        if self.rear == self.front:
            raise Exception()
        dequeue_element = self.list[self.front]
        self.front = (self.front+1)%len(self.list)
        return dequeue_element
    def output(self):
        i = self.front
        while i != self.rear:
            print(self.list[i])
            i = (i+1) % len(self.list)
myQueue = MyQueue(6)
myQueue.enqueue(3)
myQueue.enqueue(5)
myQueue.dequeue()
myQueue.output()