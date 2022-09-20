class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.rear = None
        self.front = None
        self.queue_size = 0

    def enqueue(self, val):
        # adds to the rear of the queue
        node = Node(val)
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.rear = node
            self.front = node
        self.queue_size += 1

    def dequeue(self):
        # removes from the front of the queue
        if not self.front:
            raise Exception("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        self.queue_size -= 1
        return data

    def peek(self):
        return self.front.data

    def size(self):
        return self.queue_size


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())