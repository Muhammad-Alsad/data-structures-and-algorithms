class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def to_string(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result    

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("List is empty. Cannot insert before.")
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception("Value not found. Cannot insert before.")
    
    
    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("List is empty. Cannot insert after.")
        current = self.head
        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception("Value not found. Cannot insert after.")        

if __name__ == "__main__":
    pass    