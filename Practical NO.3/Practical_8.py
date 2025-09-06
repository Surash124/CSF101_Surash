class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self.items)
    
#test
stack = stack()
stack.push("10")
stack.push("20")
stack.push("30")
stack.push("40")
stack.push("50")
print(stack.pop())
print(stack.peek())
print(stack.size())