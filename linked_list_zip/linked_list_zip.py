class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def to_string(self):
        if self.head is None:
            return "{ } -> None"
        current = self.head
        result = ""
        while current:
            result += "{ " + str(current.data) + " } -> "
            current = current.next
        result += "None"
        return result

    def merge_lists(self, list_1, list_2):
        if list_1.head is None and list_2.head is None:
            print("Both lists are empty!")
            return LinkedList()

        list_1_current = list_1.head
        list_2_current = list_2.head
        new_list = LinkedList()

        while list_1_current or list_2_current:
            if list_1_current is not None:
                new_list.append(list_1_current.data)
                list_1_current = list_1_current.next
            if list_2_current is not None:
                new_list.append(list_2_current.data)
                list_2_current = list_2_current.next
        return new_list



