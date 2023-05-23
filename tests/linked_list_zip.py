import pytest
from linked_list_zip.linked_list_zip import(
    Node, LinkedList)

def test_insert():
    linked_list = LinkedList()
    linked_list.insert(5)
    assert linked_list.head.value == 5

def test_append():
    linked_list = LinkedList()
    linked_list.append(10)
    assert linked_list.head.value == 10

def test_to_string():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.append(10)
    linked_list.append(15)
    assert linked_list.to_string() == "{ 5 } -> { 10 } -> { 15 } -> NULL"

def test_merge_lists():
    list_1 = LinkedList()
    list_1.insert(1)
    list_1.insert(3)
    
    list_2 = LinkedList()
    list_2.insert(2)
    list_2.insert(4)

    merged_list = LinkedList.merge_Lists(list_1, list_2)
    assert merged_list.to_string() == "{ 4 } -> { 2 } -> { 3 } -> { 1 } -> NULL"

def test_merge_lists_empty_lists():
    list_1 = LinkedList()
    list_2 = LinkedList()

    merged_list = LinkedList.merge_Lists(list_1, list_2)
    assert merged_list.to_string() == "Both List empty list !!"

