from math import inf

def maxLeafRoot(root):
    if not root:
        return -inf
        
    if not root.left and not root.right:
        return root.val
    return root.val + max(maxLeafRoot(root.left), maxLeafRoot(root.right))