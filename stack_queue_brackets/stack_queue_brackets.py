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



def validate_brackets(string):
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for braket in string:
        if braket in opening_brackets:
            stack.push(braket)
        elif braket in closing_brackets:
            if stack.is_empty():
                return False
            last_opening_bracket = stack.pop()
            if bracket_pairs[last_opening_bracket] != braket:
                return False

    return stack.is_empty()



if __name__=='__main__':
    print(validate_brackets("{}"))  # True
    print(validate_brackets("{[][][]}(){}"))  # True
    print(validate_brackets("()[[Extra Characters]]"))  # True
    print(validate_brackets("(){}[[]]"))  # True
    print(validate_brackets("{}{Code}[Fellows](([]))"))  # True
    print(validate_brackets("[({}[])]"))  # False
    print(validate_brackets("(]("))  # False
    print(validate_brackets("{(})"))  # False
    print(validate_brackets("[)}])"))  # False