import pytest
from linked_list_insertions.linked_list_insertions import LinkedList,Node

def test_insertion():
       
        my_list = LinkedList()
        my_list.append(1)
        assert my_list.head.value == 1

def test_append_multiple_nodes():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    actual = my_list.to_string()
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_insert_before_existing_value():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.insert_before('b', 'f')
    actual = my_list.to_string()
    expected = "{ a } -> { f } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_insert_before_head():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.insert_before('a', 'f')
    actual = my_list.to_string()
    expected = "{ f } -> { a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_insert_after_existing_value():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.insert_after('b', 'f')
    actual = my_list.to_string()
    expected = "{ a } -> { b } -> { f } -> { c } -> NULL"
    assert actual == expected