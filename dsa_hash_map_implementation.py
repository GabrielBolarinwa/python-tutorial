class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, value):
        hash_key = self.get_hash(key)
        found = False
        for i, element in enumerate(self.arr[hash_key]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_key][i] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash_key].append((key, value))

    def __getitem__(self, item):
        hash_key = self.get_hash(item)
        for element in self.arr[hash_key]:
            if element[0] == item:
                return element[1]
        return None

    def __delitem__(self, key):
        hash_key = self.get_hash(key)
        for i, item in enumerate(self.arr[hash_key]):
            if len(item) == 2 and item[0] == key:
                del self.arr[hash_key][i]


t = HashTable()
t["march 6"] = 130
t["march 17"] = 459
print(t["march 17"])
del t["march 17"]
print(t["march 17"])
