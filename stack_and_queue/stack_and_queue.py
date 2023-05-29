class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
       Pushes a new node with the specified value onto the top of the stack.

       Parameters:
         - value: The value to be stored in the new node.

        Returns:
        None
         """
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """
           Removes and returns the value of the top node from the stack.

          Raises:
          - Exception: If the stack is empty.

           Returns:
           The value of the removed node.
            """
        if not self.top:
            raise Exception("None")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Returns the value of the top node from the stack without removing it.

        Raises:
        -  Exception: If the stack is empty.

          Returns: 
          The value of the top node.
        """
        if not self.top:
            raise Exception("None")
        return self.top.value

    def is_empty(self):
        """check if the stack is empty"""
        return not bool(self.top)


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
               Adds a new node with the specified value to the rear of the queue.

    Parameters:
    - value: The value to be stored in the new node.

    Returns:
    None
        """
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
               Removes and returns the value of the front node from the queue.

    Raises:
    - Exception: If the queue is empty.

    Returns:
    The value of the removed node. 
        """
        if not self.front:
            raise Exception("None")
        value = self.front.value
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return value

    def peek(self):
        """
            Returns the value of the front node from the queue without removing it.

    Raises:
    - Exception: If the queue is empty.

    Returns:
    The value of the front node.
        """
        if not self.front:
            raise Exception("None")
        return self.front.value

    def is_empty(self):
        """
        check if queue is empty 
        """
        return not bool(self.front)



if __name__=='__main__':
    pass