import pytest
from linked_list_kth.linked_list_kth import(
    kth_from_end
) 
from linked_list.linked_list import(
    LinkedList,Node
)



def test_linkedlist_kthFromEnd_two():
    new_list2 = LinkedList()
    new_list2.insert("1")
    new_list2.insert("3")
    new_list2.insert("8")
    new_list2.insert("2")
    assert new_list2.kthFromEnd(2) == "3"    