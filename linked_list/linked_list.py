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