class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.stack_size = 0
        self.top = None
    
    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self.stack_size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.stack_size -= 1
            return data
        raise Exception("Stack is empty")

    def peek(self):
        if self.top:
            return self.top.data
        raise Exception("Stack is empty")
    
    def size(self):
        return self.stack_size

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
        