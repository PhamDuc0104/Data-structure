class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Thêm phần tử vào cuối queue

    def dequeue(self):
        if not self.items:
            print("Queue rỗng, không thể dequeue!")
            return None
        return self.items.pop(0)  # Xóa và trả về phần tử ở đầu queue

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue sau khi enqueue:", queue)
    removed = queue.dequeue()
    print("Phần tử vừa dequeue:", removed)
    print("Queue sau khi dequeue:", queue)