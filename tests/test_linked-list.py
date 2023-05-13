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
