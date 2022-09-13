from argparse import ArgumentError


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(root, path=""):
    """
    # pre-order traversal
    # you need to know the root node before you can traverse the tree
    # root -> left -> right
    """
    if not root:
        return path
    
    path += str(root.data) + "-"
    path = preorder_traversal(root.left, path)
    path = preorder_traversal(root.right, path)

    return path


def inorder_traversal(root, path=""):
    """
    # in-order traversal
    # you need to visit the left subtree, then the root, and finally the right subtree.
    # left -> root -> right
    """
    if not root:
        return path
    
    path = inorder_traversal(root.left, path)
    path += str(root.data) + "-"
    path = inorder_traversal(root.right, path)

    return path



def postorder_traversal(root, path=""):
    """
    # post-order traversal
    # you need to visit all the children of a node before you can visit the node itself
    # left -> right -> root
    """
    if not root:
        return path
    
    path = postorder_traversal(root.left, path)
    path = postorder_traversal(root.right, path)
    path += str(root.data) + "-"

    return path

if __name__ == '__main__':
    # set up tree
    """    
            _____F______
           /            \
        __D__         __I__
       /     \       /     \
       B     E       G      J
      / \            \   
      A  C           H
    """     
    root = Node("F")
    root.left = Node("D")
    root.left.left = Node("B")
    root.left.right = Node("E")
    
    root.left.left.left = Node("A")
    root.left.left.right = Node("C")
    

    root.right = Node("I")
    root.right.left = Node("G")
    root.right.left.right = Node("H")
    root.right.right = Node("J")

    print(preorder_traversal(root))
    print(inorder_traversal(root))
    print(postorder_traversal(root))
