def breadthFirst(root):
    # time complexity: O(n)
    # space complexity: O(n)
    if not root:
        return []
    
    result = []
    queue = [ root ]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        result.append(cur_node.value)

        if cur_node.left:
            queue.append(cur_node.left)
        
        if cur_node.right:
            queue.append(cur_node.right)
    return result