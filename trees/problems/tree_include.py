from pickle import FALSE


def treeInclude(root, target):
    # time complexity: O(n)
    # space complexity: O(n)
    if not root:
        return False
    
    queue =  [ root ]

    while len(queue) > 0:
        cur_node = queue.pop(0)

        if cur_node.value == target:
            return True
        
        if cur_node.left: queue.append(cur_node.left)
        if cur_node.right: queue.append(cur_node.right)
    return False 


def treeIncludeRecursive(root, target):
    # time complexity: O(n)
    # space complexity: O(n)
    if not root:
        return False
    
    if root.value == target:
        return True
    
    return treeIncludeRecursive(root.left, target) or treeIncludeRecursive(root.right, target)
