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

    def inorder(self, node):  # Xuất tăng dần
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

# Thêm các nút vào cây theo thứ tự đề bài
a = [8, 3, 5, 2, 20, 11, 30, 9, 18, 4]
tree = BST()
for x in a: tree.insert(x)
print("BST sau khi thêm các nút (inorder):", end=' ')
tree.inorder(tree.root)

# Xóa lần lượt 2 nút 5 và 20
tree.remove(5)
tree.remove(20)
print("\nBST sau khi xóa 5 và 20 (inorder):", end=' ')
tree.inorder(tree.root)