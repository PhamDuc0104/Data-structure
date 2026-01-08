class UniqueStream:
    def __init__(self):
        self.seen = set()
        self.result = []
    
    def process(self, char):
        if char not in self.seen:
            self.seen.add(char)
            self.result.append(char)
            return True
        return False
    
    def get_unique_list(self):
        return self.result
        