# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:

    DEFAULT_SIZE = 10

    def __init__(self, size = DEFAULT_SIZE):
        self.size = size
        self.data = [[], [], []]

    def __setitem__(self, index, value):
        return 0

    def __getitem__(self, index):
        return 0

    def hash(self, object):
        return hash(object) % self.size