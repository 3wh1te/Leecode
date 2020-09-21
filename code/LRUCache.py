class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.quene = []

    def get(self, key: int) -> int:
        res = self.cache.get(key, -1)
        if res == -1:
            return res
        self.quene.remove(key)
        self.quene.append(key)
        return res



    def put(self, key: int, value: int) -> None:

        if self.cache.get(key, -1) == -1:
            self.quene.append(key)
        else:
            self.quene.remove(key)
            self.quene.append(key)
        self.cache[key] = value
        if self.cache.__len__() > self.capacity:
            k = self.quene[0]
            self.quene.remove(k)
            self.cache.pop(k)
        print(self.quene)
        print(self.cache)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)