import pytest
from linked_list.linked_list import(
    LinkedList
)
from linked_list_kth.linked_list_kth import(
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

def test_linkedlist_kthFromEnd_zero():
    new_list = LinkedList()
    new_list.insert("1")
    new_list.insert("3")
    new_list.insert("8")
    new_list.insert("2")
    assert new_list.kthFromEnd(0) == "2"

def test_linkedlist_kthFromEnd_two():
    new_list2 = LinkedList()
    new_list2.insert("1")
    new_list2.insert("3")
    new_list2.insert("8")
    new_list2.insert("2")
    assert new_list2.kthFromEnd(2) == "3"

def test_linkedlist_kthFromEnd_three():
    new_list3 = LinkedList()
    new_list3.insert("1")
    new_list3.insert("3")
    new_list3.insert("8")
    new_list3.insert("2")
    assert new_list3.kthFromEnd(3) == "1"

def test_linkedlist_kthFromEnd_negative():
    new_list3 = LinkedList()
    new_list3.insert("1")
    new_list3.insert("3")
    new_list3.insert("8")
    new_list3.insert("2")
    assert new_list3.kthFromEnd(-1) == "1"

def test_linkedlist_kthFromEnd_six():
    new_list4 = LinkedList()
    new_list4.insert("1")
    new_list4.insert("3")
    new_list4.insert("8")
    new_list4.insert("2")
    assert new_list4.kthFromEnd(6) == "3"

def test_linkedlist_kthFromEnd_size_of_one():
    new_list5 = LinkedList()
    new_list5.insert("2")
    assert new_list5.kthFromEnd(0) == "2"