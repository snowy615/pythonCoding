class MyArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0
    def output(self):
        for i in range(self.size):
            print(self.array[i])
    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception()
        if self.size >= len(self.array):
            self.resize()
        for i in range(self.size - 1, -1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1
    def append(self, element):
        self.insert(self.size, element)
    def resize(self):
        array_new = [None] * len(self.array) * 2
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception()
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1
array = MyArray(4)
array.insert(0, 1)
array.insert(1, 2)
array.remove(1)
array.output()