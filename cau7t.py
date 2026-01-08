class URLStore:
    def __init__(self):
        self.urls = {}  # url -> list of timestamps
    
    def add(self, url, timestamp):
        if url not in self.urls:
            self.urls[url] = []
        self.urls[url].append(timestamp)
    
    def remove(self, url, timestamp):
        if url in self.urls:
            self.urls[url].remove(timestamp)
    
    def search(self, url):
        return self.urls.get(url, [])

# Với O(log n), có thể lưu timestamps dưới dạng balanced BST
# hoặc dùng bisect trong Python để maintain sorted list