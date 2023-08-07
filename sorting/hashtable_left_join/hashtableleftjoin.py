class Node:
    """
    A class representing a node in a linked list.

    Each node contains a value and a reference to the next node in the linked list.

    Attributes:
        value: The value stored in the node.
        next: A reference to the next node in the linked list. Default is None.


    
    """
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    """
    A class representing a linked list data structure.

    The linked list consists of nodes, each containing a value and a reference to the next node.

    Attributes:
        head: The first node in the linked list. Default is None.

    Methods:
        __init__(self, head=None):
            Initializes a new LinkedList instance.
        
        insert(self, value):
            Inserts a new node with the given value at the beginning of the linked list.
    
    
    
    """
    def __init__(self, head=None):
        self.head = head
        """
     Inserts a new node with the given value at the beginning of the linked list.

        Args:
            value: The value to be stored in the new node.

    """
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


class HashTable:
    """
         A class representing a basic hash table data structure.

    The hash table stores key-value pairs using a hash function to map keys to indices.

    Attributes:
        size: The size of the hash table (number of buckets). Default is 1024.
        buckets: A list of buckets to store key-value pairs. Each bucket may contain a linked list of pairs.
        keys: A list to store all the keys present in the hash table.

    Methods:
        __init__(self, size=1024):
            Initializes a new HashTable instance with the specified size.
    
    
    """
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size
        self.keys = []

    """
         Private method to generate a hash value for a given key.

        Args:
            key: The key for which to generate a hash value.

        Returns:
            The computed hash value.
    
    """
    def __hash(self, key):
       return sum([ord(char) for char in key]) * 283 % self.__size
    

    """
         Inserts a key-value pair into the hash table.

        Args:
            key: The key for the pair.
            value: The value associated with the key. 
    
    """
    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = LinkedList()
            self.__buckets[index] = ll
        self.__buckets[index].insert([key, value])
        self.keys.append(key)
        """
              Retrieves the value associated with a given key from the hash table.

        Args:
            key: The key for which to retrieve the value.

        Returns:
            The value associated with the key, or None if the key is not found.
        
        """

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
    
    """
       Checks if a given key exists in the hash table.

        Args:
            key: The key to check.

        Returns:
            True if the key exists, False otherwise.  
    
    """
    def has(self, key):
        if self.get(key):
            return True
        return False
    """
        Returns a list of all keys present in the hash table.

        Returns:
            A list of keys.
    
    """
    def keys(self):
        return self.keys
    """
         Performs a left join operation on two hashmaps, combining their values based on matching keys.

    This function takes two hashmaps as input and performs a left join operation on them.
    It combines the values from hashmap1 and hashmap2 for matching keys and returns the result.

    Args:
        hashmap1: The first hashmap.
        hashmap2: The second hashmap.

    Returns:
        A list of lists containing combined key-value pairs from hashmap1 and hashmap2.
        Each inner list has the format [key, value_from_hashmap1, value_from_hashmap2].
    
    """
    
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
