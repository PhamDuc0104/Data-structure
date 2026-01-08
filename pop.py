class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Thêm phần tử vào đỉnh stack

    def pop(self):
        if not self.items:
            print("Stack rỗng, không thể pop!")
            return None
        return self.items.pop()  # Xóa và trả về phần tử ở đỉnh stack

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack sau khi push:", stack)
    popped = stack.pop()
    print("Phần tử vừa pop:", popped)
    print("Stack sau khi pop:", stack)