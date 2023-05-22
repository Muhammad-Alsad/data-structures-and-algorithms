class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next
    def __str__(self):
        return self.value     
        


class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def to_string(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result        


    @staticmethod
    def merge_Lists(list_1,list_2):
        if list_1.head == None and list_2 == None:
            print("Both List empty list !!")
        list_1_current = list_1.head
        list_2_current = list_2.head
        new_list = LinkedList()
        while list_1_current or list_2_current:
            if list_1_current is not None:
                new_list.append(list_1_current)
                list_1_current = list_1_current.next
            if list_2_current is not None:
                new_list.append(list_2_current)
                list_2_current = list_2_current.next
        return new_list
            
if __name__ == "__main__":
    list_1 = LinkedList()
    list_1.insert("2")
    list_1.insert("3")
    list_1.insert("1")
    list_2 = LinkedList()
    list_2.insert("9")
    list_2.insert("5")
    list_2.insert("3")
    list_2.insert("2")
    # print(ll2.to_string())
    list_3 = LinkedList.merge_Lists(list_1,list_2)
    print(list_3.to_string())

   

