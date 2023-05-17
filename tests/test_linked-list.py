import pytest
from linked_list.linked_list import(
    LinkedList
)

def test_insert_into_linked_list():
    my_list = LinkedList()
    my_list.insert('a')
    actual = my_list.head.value
    expected = 'a'
    assert actual == expected

def test_insert_into_linked_list1():
    my_list = LinkedList()
    my_list.insert('b')
    actual = my_list.head.value
    expected = 'b'
    assert actual == expected

def test_linkedlist_instantiattion_empty():
    new_list = LinkedList()
    actual = (new_list.head == None)
    expected = True
    assert actual == expected

def test_linkedlist_insertion_by_function():
    new_list = LinkedList()
    new_list.insert("Georgia")
    head = new_list.head.value
    actual = head
    expected = "Georgia"
    assert actual == expected

