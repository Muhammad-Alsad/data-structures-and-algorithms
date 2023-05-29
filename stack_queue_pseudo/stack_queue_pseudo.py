class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()  
        self.stack2 = Stack() 

    def enqueue(self, value):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        if self.stack1.is_empty():
            raise IndexError("PseudoQueue is empty")
        return self.stack1.pop()
    
    
    
if __name__=="__main__":
    q = PseudoQueue()

    q.enqueue(10)
    q.enqueue(15)
    q.enqueue(20)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    
    

   
   