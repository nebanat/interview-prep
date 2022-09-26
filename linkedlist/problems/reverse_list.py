def reverse_linked_list(head):
    # we need an initial prev
    prev = None 
    cur_node = head 
    
    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev
        prev = cur_node
        cur_node = next_node
      
    return prev

def reverse_linked_list_recursive(head, prev=None):
    if not head:
        return prev
    next_node = head.next
    head.next = prev
    return reverse_linked_list(next_node, head)


    # N    a  ->  b -> c 
    
    #       prev  cur  next