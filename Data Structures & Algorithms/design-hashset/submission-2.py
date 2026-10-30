class MyHashSet:

    def __init__(self):
        self.seen = []
        
    def add(self, key: int) -> None:
        if key not in self.seen:
            self.seen.append(key)
        else:
            pass

    def remove(self, key: int) -> None:
        if key in self.seen:
            self.seen.remove(key)
        else:
            pass

    def contains(self, key: int) -> bool:
        if key in self.seen:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)