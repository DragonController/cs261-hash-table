# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:

    DEFAULT_SIZE = 10

    def __init__(self, size = DEFAULT_SIZE):
        self.size = size
        self.data = []
        for _ in range(self.size):
            self.data.append([])

    def __setitem__(self, key, value):
        exist = False
        for index in range(len(self.data[self.hash(key)])):
            if self.data[self.hash(key)][index][0] == key:
                self.data[self.hash(key)][index] = [key, value]
                exist = True
        if not exist:
            self.data[self.hash(key)].append([key, value])

    def __getitem__(self, key):
        for index in range(len(self.data[self.hash(key)])):
            if self.data[self.hash(key)][index][0] == key:
                return self.data[self.hash(key)][index][1]
        return None

    def hash(self, object):
        return hash(object) % self.size

    def delete(self, key):
        for index in range(len(self.data[self.hash(key)])):
            if self.data[self.hash(key)][index][0] == key:
                self.data[self.hash(key)][index] = [None]
    
    def clear(self):
        for index in range(self.size):
            self.data[index] = []

    def keys(self):
        keys = []
        for index1 in range(len(self.data)):
            for index2 in range(len(self.data[index1])):
                keys.append(self.data[index1][index2][0])
        return keys

    def values(self):
        values = []
        for index1 in range(len(self.data)):
            for index2 in range(len(self.data[index1])):
                values.append(self.data[index1][index2][1])
        return values
    