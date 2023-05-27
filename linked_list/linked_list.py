class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert (self , value):
         new_node = Node(value)
         if self.head is None:
            self.head = new_node
         else:
             new_node.next = self.head
             self.head = new_node  
    
    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result          
    

if __name__ == "__main__":
    
    my_list = LinkedList()


    my_list.insert('d')
    my_list.insert('c')
    my_list.insert('b')
    my_list.insert('a')


    print(my_list.includes('b'))  
    print(my_list.includes('d'))  
    print(my_list.includes('f')) 

    print(my_list.to_string())    