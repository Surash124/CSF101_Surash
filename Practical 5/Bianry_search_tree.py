#Definiing the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Binary search tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None
#Insertion Method 
    def insert(self, value):
        if not self.root:
            self.root = Node(Value)
        else:
            self._insert_recursive(self.root, value)
        def _insert_recursive(self, node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self._insert_recursive(node.left, value)
            else:
                if node.right is None:
                 node.right = Node(value)
                else:
                self._insert_recursive(node.right, value)

bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)
class BinarySearchTree:
    # ... (previous code)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
print(bst.search(4))
print(bst.search(9))