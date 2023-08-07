class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)


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

    def left_join(hashmap1, hashmap2):
        if not hashmap1:
            raise ValueError("Left hashmap is empty")

        all_keys = set(hashmap1.keys()) | set(hashmap2.keys())

        result = []
        for key in all_keys:
            entry = [key]
            entry.append(hashmap1.get(key, None))
            entry.append(hashmap2.get(key, None))
            result.append(entry)

        return result    
    


def tree_intersection(tree1, tree2):
        values_set1 = hashmap_tree_values(tree1)
        values_set2 = hashmap_tree_values(tree2)

        intersection_set = values_set1.intersection(values_set2)
        return intersection_set

def hashmap_tree_values(tree):
        values_set = set()
        if not tree:
            return values_set

        stack = [tree.root]
        while stack:
            node = stack.pop()
            values_set.add(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return values_set
    




hashmap1 = {
    'apple': "red",
    'banana': "green",
    'orange': "orange"
}

hashmap2 = {
    'banana': 'yellow',
    'kiwi': 'green',
    'grape': 'purple'
}

result = HashTable.left_join(hashmap1, hashmap2)

print(result)