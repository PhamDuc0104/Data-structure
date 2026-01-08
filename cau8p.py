class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, x):
    if root is None:
        return None
    if root.data == x:
        return root
    elif x < root.data:
        return search(root.left, x)
    else:
        return search(root.right, x)

# Tạo cây
root = Node(70)
root.left = Node(65)
root.right = Node(75)
root.left.left = Node(40)
root.left.right = Node(72)
root.right.left = Node(58)
root.right.right = Node(88)
root.left.left.left = Node(36)
root.left.left.right = Node(54)
root.right.left.right = Node(45)
root.right.right.left = Node(45)
root.right.right.right = Node(90)

x = 47
result = search(root, x)
if result:
    print(f"Tìm thấy node {x}")
else:
    print(f"Không tìm thấy node {x}")
