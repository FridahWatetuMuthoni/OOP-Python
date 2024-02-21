class MaxSizeList:
    def __init__(self, max):
        self.max = max
        self.list = []
    
    def push(self, value):
        self.list.append(value)
        if(len(self.list) > self.max):
            self.list.remove(self.list[0])
    
    def get_list(self):
        return self.list