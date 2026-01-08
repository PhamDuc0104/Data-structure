# Định nghĩa node cây
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Hàm tìm kiếm trong cây nhị phân
def search(root, x):
    if root is None:
        return None
    if root.data == x:
        return root
    elif x < root.data:
        return search(root.left, x)
    else:
        return search(root.right, x)

# Tạo cây theo đề
root = Node(30)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(10)
root.left.right = Node(24)
root.right.left = Node(34)
root.right.right = Node(46)
root.left.left.left = Node(6)
root.left.left.right = Node(14)
root.left.right.left = Node(22)
root.left.right.right = Node(27)

x = 22
result = search(root, x)
if result:
    print(f"Tìm thấy node có giá trị {x}")
else:
    print(f"Không tìm thấy node {x}")
