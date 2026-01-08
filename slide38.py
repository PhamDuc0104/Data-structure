class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):  # Init
        self.root = None

    def is_empty(self):  # IsEmpty
        return self.root is None

    def create_node(self, key):  # CreateNode
        return Node(key)

    def insert(self, key):  # Insert
        def _ins(node, key):
            if not node: return Node(key)
            if key < node.key:
                node.left = _ins(node.left, key)
            else:
                node.right = _ins(node.right, key)
            return node
        self.root = _ins(self.root, key)

    def remove(self, key):  # Remove
        def _remove(node, key):
            if not node: return None
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                if not node.left: return node.right
                if not node.right: return node.left
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.key = temp.key
                node.right = _remove(node.right, temp.key)
            return node
        self.root = _remove(self.root, key)

    def clear_tree(self):  # ClearTree
        self.root = None

    def inorder(self, node):  # Xuất tăng dần
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def reverse_inorder(self, node):  # Xuất giảm dần
        if node:
            self.reverse_inorder(node.right)
            print(node.key, end=' ')
            self.reverse_inorder(node.left)

# Ví dụ sử dụng
a = [7, 3, 9, 1, 5, 8, 10]
tree = BST()
for x in a: tree.insert(x)
print("BST rỗng?", tree.is_empty())
print("Xuất tăng dần:", end=' '); tree.inorder(tree.root)
print("\nXuất giảm dần:", end=' '); tree.reverse_inorder(tree.root)
tree.remove(9)
print("\nSau khi xóa 9, tăng dần:", end=' '); tree.inorder(tree.root)
tree.clear_tree()
print("\nSau khi clear, BST rỗng?", tree.is_empty())