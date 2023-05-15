import pytest
from linked_list_insertions.linked_list_insertions import LinkedList,Node

def test_insertion():
       
        my_list = LinkedList()
        my_list.append(1)
        assert my_list.head.value == 1