class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Thêm phần tử vào đỉnh stack

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack sau khi push:", stack)