def list_find(head, target):
    # time complexity: O(n)
    # space complexity: O(1)
    cur_node = head

    while cur_node:
        if cur_node.value == target:
            return True
        cur_node = cur_node.next
    return False

def list_find_recursive(head, target):
    # time complexity: O(n)
    # space complexity: O(n)
    if not head:
        return False
    
    if head.value == target:
        return True
    
    return list_find_recursive(head.next, target)
    