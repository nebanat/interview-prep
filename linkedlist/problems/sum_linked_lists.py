# TODO
# 2 -> 4  -> 7 -> 1
# 9 -> 4 -> 5 
# current_1 = 1
# current_2 = 0
# carry = 1 
# 0 -> 1 -> 9 -> 2 -> 2

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

def sumLinkedList(head, head2):
    r_linked_list = LinkedList()
    r_linked_list.head = Node(0)
    cur_node = r_linked_list.head
    
    cur_one = head
    cur_two = head2
    carry = 0

    while cur_one or cur_two or carry:
        value_one = cur_one.value if cur_one else 0
        value_two = cur_two.value if cur_two else 0
        sum_value = value_one + value_two + carry

        new_value = sum_value % 10 
        cur_node.next = Node(new_value)
        cur_node = Node(new_value)

        carry = sum_value // 10

        value_one = cur_one.next if cur_one else None 
        value_two = cur_two.next if cur_two else None
    
    r_linked_list.head = r_linked_list.head.next

    return r_linked_list