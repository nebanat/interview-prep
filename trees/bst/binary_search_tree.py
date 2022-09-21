class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Value already in tree")
    

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    
    def _find(self, data, current_node):
        if data > current_node.data and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.data and current_node.left:
            return self._find(data, current_node.left)
        if data == current_node.data:
            return True
    
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
    
    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def is_bst_satisfied(self):
      if not self.root:
        return True 
      return self._is_bst_satisfied(self.root)
    
    def _is_bst_satisfied(self, cur_node):
        if cur_node.left:
            if cur_node.data > cur_node.left.data:
                return  self._is_bst_satisfied(cur_node.left)
            else:
                return False
        if cur_node.right:
            if cur_node.data < cur_node.right.data:
                return self._is_bst_satisfied(cur_node.right)
            else:
                return False
        
        return True

if __name__ == "__main__":
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(5)
    bst.insert(10)

    tree = BST()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    print(bst.inorder_print_tree())
    print(bst.is_bst_satisfied())
    print(tree.is_bst_satisfied())
    # print(bst.find(10))
    # print(bst.find(12))