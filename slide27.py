class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

class BST:
    def __init__(self): self.root = None
    def insert(self, key):
        def _ins(n, k):
            if not n: return Node(k)
            if k < n.key: n.left = _ins(n.left, k)
            else: n.right = _ins(n.right, k)
            return n
        self.root = _ins(self.root, key)
    def inorder(self, n):  # LNR
        if n: self.inorder(n.left); print(n.key, end=' '); self.inorder(n.right)
    def preorder(self, n): # NLR
        if n: print(n.key, end=' '); self.preorder(n.left); self.preorder(n.right)
    def postorder(self, n):# LRN
        if n: self.postorder(n.left); self.postorder(n.right); print(n.key, end=' ')
    def level_order(self):
        q = [self.root]
        while q:
            n = q.pop(0)
            if n: print(n.key, end=' '); q += [n.left, n.right]
    def search(self, n, x):
        if not n: return False
        if n.key == x: return True
        return self.search(n.left, x) if x < n.key else self.search(n.right, x)
    def height(self, n):
        return 0 if not n else 1 + max(self.height(n.left), self.height(n.right))
    def count_nodes(self, n):
        return 0 if not n else 1 + self.count_nodes(n.left) + self.count_nodes(n.right)
    def count_leaves(self, n):
        if not n: return 0
        if not n.left and not n.right: return 1
        return self.count_leaves(n.left) + self.count_leaves(n.right)

a = [7, 3, 9, 1, 5, 8, 10]
tree = BST()
for x in a: tree.insert(x)
print("LNR:", end=' '); tree.inorder(tree.root)
print("\nNLR:", end=' '); tree.preorder(tree.root)
print("\nLRN:", end=' '); tree.postorder(tree.root)
print("\nLevel:", end=' '); tree.level_order()
print("\nTìm 5:", "Có" if tree.search(tree.root, 5) else "Không")
print("Cao:", tree.height(tree.root))
print("Số node:", tree.count_nodes(tree.root))
print("Số lá:", tree.count_leaves(tree.root))