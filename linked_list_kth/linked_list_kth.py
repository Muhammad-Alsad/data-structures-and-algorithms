def kth_from_end(self, k):
    temp_lst = []
    current = self.head
    while current is not None:
        temp_lst.append(current.value)
        current = current.next
        
    if k >= len(temp_lst):
        raise ValueError(f'Linked list has fewer than {k} elements.')
        
    return temp_lst[-k-1]

