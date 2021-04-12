class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        self.items.move_to_end(key)
        return self.items[key]

    def put(self, key: int, value: int) -> None:
        if len(self.items) == self.capacity and key not in self.items:
            self.items.popitem(last=False)
        self.items[key] = value
        self.items.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)