class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)


# Example usage
bst = BinarySearchTree()
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = bst.insert(root, key)

print("Inorder Traversal:")
bst.inorder_traversal(root)
