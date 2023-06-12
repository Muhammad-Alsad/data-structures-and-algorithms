from trees.stack_and_queue import Queue

class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class Tnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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


class BinarySearch(Tree):
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
            raise ValueError("You Should Type A Number !")
        
    def add(self,value):

        if self.contains(value):
            raise ValueError("The value is already Exist in the Tree !")
        
        if self.root is None:
            self.root = Tnode(value)
            return
        
        root = self.root
        while root is not None:
            if value < root.value:
                if root.left is None:
                    root.left = Tnode(value)
                    return
                root = root.left

            elif value > root.value:
                if root.right is None:
                    root.right = Tnode(value)
                    return
                root = root.right
    def tree_max():
        pass                

if __name__ == "__main__":
    tree = Tree()
    tree.root = Tnode("A")
    tree.root.left = Tnode("B")
    tree.root.right = Tnode("C")
    tree.root.left.left = Tnode("D")
    tree.root.left.right = Tnode("E")
    tree.root.right.left = Tnode("F")

   
    print(tree.pre_order())
    print(" ")
    print(tree.in_order())
    print(" ")
    print(tree.post_order())
