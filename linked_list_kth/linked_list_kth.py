class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def append(self, value):
        if self.head is None:
            self.insert(value)
            return
        new_node = Node(value)
        current = self.head
        while current is not None:
            if current.next is None:
                current.next = new_node
                new_node.next = None
            current = current.next        

    def kthFromEnd(self,k):
        try:
            lst_temp = []
            current = self.head
            while current != None:
                lst_temp.append(current.value)
                current = current.next
            
            if k <= len(lst_temp):
                return lst_temp[k]
            else:
                raise ValueError
        except ValueError as ve:
            print(ve)
            raise ValueError(f'Linked list has Less than {k} elements.')

