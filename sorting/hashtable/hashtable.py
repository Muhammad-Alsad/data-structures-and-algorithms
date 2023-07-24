class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size
        self.keys = []

    def __hash(self, key):
        hash_value = 0
        prime = 101
        for char in key:
            hash_value = (hash_value * prime + ord(char)) % self.__size
        return hash_value
    
    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = LinkedList()
            self.__buckets[index] = ll

        self.__buckets[index].insert([key, value])
        self.keys.append(key)

    def get(self, key):
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            curr = bucket.head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
        return None

    def has(self, key):
        if self.get(key):
            return True
        return False

    def keys(self):
        return self.keys

    @staticmethod
    def repeated_word(string):
        words = string.replace(",", "").lower().split()
        word_table = HashTable()
        for word in words:
            if word_table.has(word):
                return word
            word_table.set(word, 1)
        return None
