from collections import deque

stack = deque()

# adding element
stack.append(10)
stack.append(20)

# printing stack
print("Initial Stack..")
print(stack)

print("Element that are pop from stack.")
print(stack.pop())
print(stack.pop())
