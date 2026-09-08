# import csv
from encryption_program import index

# with open("test/nyc_weather.csv", mode="r") as f:
#     csv_data = csv.reader(f)
#     total = 0
#     next(csv_data)
#     temps = []
#     for i, row in enumerate(csv_data):
#         temps.append(int(row[1]))
#
#     avg = sum(temps[0:7]) / len(temps[0:7])
#     print(avg)
#     max_num = max(temps[0:10])
#     print(max_num)

# temp_dict = {}
#
# with open("test/nyc_weather.csv", mode="r") as f:
#     csv_data = csv.reader(f)
#     next(csv_data)
#     for row in csv_data:
#         temp_dict[row[0]] = row[1]
#
# print(temp_dict["Jan 9"])
# print(temp_dict["Jan 4"])

# word_count = {}
# with open("test/poem.txt", mode="r") as f:
#     for line in f:
#         words = line.split(" ")
#         for word in words:
#             word = word.replace("\n", "")
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
#
# print(word_count)


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]
        self.TOMBSTONE = "Deleted"

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, value):
        hash_key = self.get_hash(key) % self.MAX
        while self.arr[hash_key] is not None and self.arr[hash_key] != self.TOMBSTONE:
            if self.arr[hash_key][0] == key:
                self.arr[hash_key] = (key, value)
                return
            hash_key= (hash_key+1) % self.MAX
        self.arr[hash_key] = (key, value)

    def __getitem__(self, item):
        hash_key = self.get_hash(item) % self.MAX
        while self.arr[hash_key] is not None:
            if self.arr[hash_key] != self.TOMBSTONE and self.arr[hash_key][0] == item:
                return self.arr[item][1]
            hash_key = (hash_key+1) % self.MAX
        return None

    def __delitem__(self, key):
        hash_key = self.get_hash(key)
        while self.arr[hash_key] is not None:
            if self.arr[hash_key] != self.TOMBSTONE and self.arr[hash_key][0] == key:
                self.arr[hash_key] = self.TOMBSTONE
                return
            hash_key = (hash_key + 1) % self.MAX

table = HashTable()
table["march 6"]