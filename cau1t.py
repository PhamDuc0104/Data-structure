def find_pairs_with_sum(root, k):
    # Duyệt inorder để có danh sách sorted
    nodes = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            nodes.append(node.value)
            inorder(node.right)
    
    inorder(root)
    
    # Two pointer approach
    left = 0
    right = len(nodes) - 1
    pairs = []
    
    while left < right:
        current_sum = nodes[left] + nodes[right]
        if current_sum <= k:
            pairs.append((nodes[left], nodes[right]))
            left += 1
        else:
            right -= 1
    
    return pairs