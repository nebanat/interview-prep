def tree_recursive(root):
    # time: O(n)
    # space: O(n)
    if not root:
        return 0
    
    # this is with explicit total
    # total += root.value
    # total += tree_recursive(root.left, total)
    # total += tree_recursive(root.right, total)

    return root.value + tree_recursive(root.left) + tree_recursive(root.right)


def tree_recursive_iterative(root):
    if not root:
        return 0
    
    total = 0
    queue = [ root ]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        total += cur_node.value

        if cur_node.left:
            queue.push(cur_node.left)
        
        if cur_node.right:
            queue.push(cur_node.right)
    return total
        