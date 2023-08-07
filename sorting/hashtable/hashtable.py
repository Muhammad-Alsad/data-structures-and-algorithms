class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        try:
            if self.top is not None:
                temp = self.top
                self.top = temp.next
                temp.next = None
                return temp.value
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError("Stack is empty")

    def peek(self):
        try:
            if self.top is not None:
                return self.top.value
                
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError(f"Stack is empty")

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


class Queue:
    def __init__(self, back=None, front=None):
        self.back = back
        self.front = front

    def enqueue(self, value):
        new_node = Node(value)

        if self.front == None:
            self.back = new_node
            self.front = new_node
            self.back.next = None
            self.front.next = None
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        try:
            if self.front is not None:
                temp = self.front
                self.front = temp.next
                temp.next = None
                return temp.value
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError("Queue is empty")

    def peek(self):
        try:
            if self.front is not None:
                return str(self.front.value)
            else:
                raise ValueError

        except ValueError as ve:
            print(ve)
            raise ValueError(f"Queue is empty")

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False


class Tree:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            if front.left is not None:
                queue.enqueue(front.left)

            if front.right is not None:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        output = []

        def _walk(root):
            output.append(root.value)

            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            output.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def post_order(self):
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            output.append(root.value)

        _walk(self.root)
        return output


class BinaryTree(Tree):
    def __init__(self):
        self.root = None
    def contains(self, value):
        try:
            is_found = False
            root = self.root

            while root is not None:
                if value == root.value:
                    is_found = True
                    return is_found

                if value < root.value:
                    root = root.left
                else:
                    root = root.right
            return is_found
        except TypeError:
            raise ValueError("Value must be a number!")
        
    def add(self,value):

        if self.contains(value):
            raise ValueError("The value is already in the Tree!")
        
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        root = self.root
        while root is not None:
            if value < root.value:
                if root.left is None:
                    root.left = TreeNode(value)
                    return
                root = root.left

            elif value > root.value:
                if root.right is None:
                    root.right = TreeNode(value)
                    return
                root = root.right


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
    

def tree_intersection(t1, t2):
    hash_table = HashTable()
    output = []
    result = []
    
    root = t1.root
    def _hash_tree_1(root):
        if root:
            _hash_tree_1(root.left)
            output.append(root.value)
            hash_table.set(root.value, "added")
            _hash_tree_1(root.right)

    _hash_tree_1(root)
    
    root = t2.root
    def traverse_tree_2(root):
        if root:
            traverse_tree_2(root.left)
            if hash_table.has(root.value):
                result.append(root.value)
            traverse_tree_2(root.right)

    traverse_tree_2(root)
    
    return result


<<<<<<< HEAD
=======
if __name__ == "__main__":

    tree = BinaryTree()
    tree2 = BinaryTree()
    
    tree.root = TreeNode("150")
    tree.root.left = TreeNode("100")
    tree.root.right = TreeNode("250")
    tree.root.left.left = TreeNode("75")
    tree.root.left.right = TreeNode("160")
    tree.root.left.right.left = TreeNode("125")
    tree.root.left.right.right = TreeNode("175")
    tree.root.right.left = TreeNode("200")
    tree.root.right.right = TreeNode("350")
    tree.root.right.right.left = TreeNode("300")
    tree.root.right.right.right = TreeNode("500")
    
    tree2.root = TreeNode("42")
    tree2.root.left = TreeNode("100")
    tree2.root.right = TreeNode("600")
    tree2.root.left.left = TreeNode("15")
    tree2.root.left.right = TreeNode("160")
    tree2.root.left.right.left = TreeNode("125")
    tree2.root.left.right.right = TreeNode("175")
    tree2.root.right.left = TreeNode("200")
    tree2.root.right.right = TreeNode("350")
    tree2.root.right.right.left = TreeNode("4")
    tree2.root.right.right.right = TreeNode("500")
>>>>>>> main


    print(tree_intersection(tree,tree2)) # == ["100","160","125","175","200","350","500"]

