class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def isEmpty(self):
        return  self.stack == []

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    # def stackSize(self):
    #     return len(self.stack)
    