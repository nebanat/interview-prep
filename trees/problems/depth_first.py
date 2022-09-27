def depthFirst(root):
    if not root:
        return [] 

    result = []
    stack = [ root ]

    while len(stack) > 0:
        cur_node = stack.pop()
        result.append(cur_node.value)

        if cur_node.right: stack.append(cur_node.right)
        if cur_node.left: stack.append(cur_node.left)
    
    return result


def depthFirstRecursive(root):
    if not root:
        return []
    left_values = depthFirstRecursive(root.left) # b, d, e
    right_values = depthFirstRecursive(root.right) # c, f

    return [root.value] + left_values + right_values