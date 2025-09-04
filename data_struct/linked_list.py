class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None
    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception()
        p = self.head
        for i in range(index):
            p = p.next
        return p
    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise Exception()
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.last = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif self.size == index:
            self.last.next = node
            self.last = node
        else:
            prev_node = self.get(index-1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception()
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            prev_node = self.get(index-1)
            removed_node = prev_node.next
            prev_node.next = None
            self.last = prev_node
        else:
            prev_node = self.get(index-1)
            next_node = prev_node.next.next
            removed_node = prev_node.next
            prev_node.next = next_node
            self.size -= 1
            return removed_node
    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next
linkedList = LinkedList()
linkedList.insert(1, 0)
linkedList.insert(2, 0)
linkedList.remove(0)
linkedList.output()