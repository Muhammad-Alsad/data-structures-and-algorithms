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


def test_linkedlist_insertion_by_function():
    new_list = LinkedList()
    new_list.insert("Georgia")
    head = new_list.head.value
    actual = head
    expected = "Georgia"
    assert actual == expected

# @pytest.mark.skip(reason="Done")
def test_linkedlist_head_points_to_first_node_():
    new_list = LinkedList()
    new_list.insert("London")
    new_list.insert("Paris")
    new_list.insert("Amsterdam")
    new_list.insert("Manila")
    new_list.insert("Tokyo")
    head = new_list.head.value
    actual = head
    expected = "Tokyo"
    assert actual == expected

# @pytest.mark.skip(reason="Done")
def test_linkedlist_includes_():
    new_list = LinkedList()
    new_list.insert("Berlin")
    new_list.insert("Istanbul")
    new_list.insert("Zegreb")
    assert new_list.includes("Berlin") == True
    assert new_list.includes("Moscow") == False

def test_linked_list():
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    my_list.insert('d')
    actual = (my_list.head.value, my_list.head.next.value, my_list.head.next.next.value)
    expected =  ('d', 'c', 'b') 
    assert actual == expected
    

