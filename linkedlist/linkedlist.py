class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
    
    def set_head(self, node):
        if not self.head:
            self.head = node
        else:
            current_head = self.head
            self.head = node
            self.head.next = current_head
            current_head.prev = self.head
        # return self.head