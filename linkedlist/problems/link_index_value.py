def getNodeValue(head, index):
    # Time complexity: O(n)
    # space complexity: O(1)
    count = 0
    cur_node = head

    while cur_node:
        if count == index:
            return cur_node.value
        cur_node = cur_node.next
        count += 1
    return None

def getNodeValueRecursive(head, index):
    # Time complexity: O(n)
    # space complexity: O(n)
    if not head:
        return None 
        
    if index == 0:
        return head.value
    return getNodeValueRecursive(head.next, index - 1)