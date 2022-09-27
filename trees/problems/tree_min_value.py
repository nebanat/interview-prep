from math import inf
from turtle import right

def treeMinValue(root):
    min_value = inf
    stack = [ root ]

    while len(stack) > 0:
        cur_node = stack.pop()

        if cur_node.value < min_value:
            min_value = cur_node.value

        if cur_node.left:
            stack.push(cur_node.left)
        
        if cur_node.right:
            stack.push(cur_node.right)
    
    return min_value

def treeMinValueRecursive(root):
    if not root:
        return inf
    left_min = treeMinValueRecursive(root.left)
    right_min = treeMinValueRecursive(root.right)
    return min(root.value, left_min, right_min)