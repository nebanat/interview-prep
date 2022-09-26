# Linkedlist
# - Does not require elements to be stored in contiguous memory
# - Insertion operation O(1) is way more efficient than that of a array/list O(n)
#   because you just need to update the node pointers
# - when traversing linkedlist always stay in the present to avoid code clogging

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

def traversal(head):
    cur_node = head

    while cur_node:
        print(cur_node.value)
        cur_node = cur_node.next

def traversal_recursive(node):
    if not node:
        return 
    print(node.value)
    traversal_recursive(node.next)


if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    # A -> B -> C -> D -> None
    a.next = b
    b.next = c 
    c.next = d
    traversal(a)
    traversal_recursive(a)