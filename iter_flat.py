class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = nested_list[::-1]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.stack:
            high = self.stack.pop()
            if isinstance(high, list):
                self.stack.extend(high[::-1])
            else:
                return high
        raise StopIteration
    
nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)
