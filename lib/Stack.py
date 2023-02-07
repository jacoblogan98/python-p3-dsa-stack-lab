class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit

        for item in items:
            if (not self.full()):
                self.items.append(item)

    def isEmpty(self):
        return True if not self.items else False 

    def push(self, item):
        self.items.insert(0, item) if not self.full() else "The stack is full"

    def pop(self):
        if self.isEmpty(): return None
        
        return self.items.pop(0)

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() >= self.limit:
            return True
        else: 
            return False

    def search(self, target):
        for i in range(self.size()):
            if self.items[i] == target: return i
        
        return -1
