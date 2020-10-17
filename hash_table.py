# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:

    DEFAULT_SIZE = 10

    def __init__(self, size = DEFAULT_SIZE):
        self.size = size
        self.data = [[], [], []]

    def __setitem__(self, key, value):
        self.data = [[], [], [[key, value]]]

    def __getitem__(self, key):
        return 0

    def hash(self, object):
        return hash(object) % self.size