class Stack(object):
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, data):
        if self.top >= self.size - 1:
            print("Stack is overflow..")
        else:
            self.top += 1
            self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack is underflow.")
            return
        else:
            self.stack[self.top] = None
            self.top -= 1

    def display(self):
        if self.top <= -1:
            print("Stack is underflow..")
        else:
            for i in range(self.top,-1,-1):
                print(self.stack[i])



stack = Stack(3)
stack.display()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()