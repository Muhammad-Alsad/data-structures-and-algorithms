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
       return sum([ord(char) for char in key]) * 283 % self.__size
    
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
    
def left_join(hashmap1, hashmap2):
        if not hashmap1:
            raise ValueError("Left hashmap is empty")
        hashmapkey = hashmap1.keys

        Keys = []
        
        for key in hashmapkey:
            if key not in Keys:
                Keys.append(key)
                
        result = []
        for key in Keys:
            entry = [key]
            entry.append(hashmap1.get(key))
            entry.append(hashmap2.get(key))
            result.append(entry)
        return result    
    




if __name__=="__main__":
    # hashmap1 = HashTable()
    # hashmap2 = HashTable()

    # hashmap1.set('apple', 'red')
    # hashmap1.set('banana', 'green')
    # hashmap1.set('orange', 'orange')

    # hashmap2.set('banana', 'yellow')
    # hashmap2.set('kiwi', 'green')
    # hashmap2.set('grape', 'purple')

    # result = left_join(hashmap1, hashmap2)

    hash_partners1 = HashTable()
    hash_partners2 = HashTable()

    hash_partners1.set('Alice', 'Bob')
    hash_partners1.set('Eve', 'John')

    hash_partners2.set('Eve', 'Michael')
    hash_partners2.set('Mia', 'Daniel')

    result1 = left_join(hash_partners1, hash_partners2)
    print(result1)
