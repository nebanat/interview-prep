class Stack:
    # Last in First out 
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
class Queue:
    # First in First Out
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def deque(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)



if __name__ == '__main__':
    # stack 
    # stack = Stack()
    # stack.push(10)
    # stack.push(12)
    # stack.push(13)
    # print(stack.pop())

    # queue 
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(12)
    queue.enqueue(13)
    print(queue.deque())
