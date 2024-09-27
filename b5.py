class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, value):
        if not self.is_full():
            self.stack.append(value)
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def count(self):
        return len(self.stack)

# Chương trình chính
stack = Stack(5)
stack.push(1)
stack.push(2)
print("Number of elements:", stack.count())  # Output: 2
