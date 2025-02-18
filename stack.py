from collections.abc import MutableSequence


class Stack:
    def __init__(self):
        self.stack: MutableSequence = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        top = self.stack[-1]
        self.stack.remove(top)
        return top

    def peek(self):
        return self.stack[-1]
    
    def print(self):
        print(self.stack)

if __name__ == '__main__':
    stack: Stack = Stack()
    stack.print()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()

    stack.peek()
    stack.print()

    stack.pop()
    stack.print()
