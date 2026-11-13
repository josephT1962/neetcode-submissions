class MyHashSet:

    def __init__(self):
        self.key=[]

    def add(self, key: int) -> None:
        if key not in self.key:
            self.key.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.key)):
            if self.key[i]==key:
                self.key[i]=[]

    def contains(self, key: int) -> bool:
        for i in self.key:
            if i==key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)