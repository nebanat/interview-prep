class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def traversal(head):
    if not head:
        return 
    
    print(head.data)
    traversal(head.next)

if __name__ == '__main__':
    head = Node("dog", Node("cat", Node("rat")))
    # item1 = Node("dog")
    # item2 = Node("cat")
    # item3 = Node("rat")

    # item1.next = item2
    # item2.next = item3

    traversal(head)