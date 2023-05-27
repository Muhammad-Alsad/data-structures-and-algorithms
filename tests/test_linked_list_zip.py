import pytest
from linked_list.linked_list import(
    LinkedList)
from linked_list_zip.linked_list_zip import(
     LinkedList)

def test_merge_lists_one():
    ll1 = LinkedList()
    ll1.insert("2")
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    ll2.insert("4")
    ll2.insert("9")
    ll2.insert("5")
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> None"


def test_merge_lists_two():
    ll1 = LinkedList()
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    ll2.insert("4")
    ll2.insert("9")
    ll2.insert("5")
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> None"


def test_merge_lists_three():
    ll1 = LinkedList()
    ll1.insert("2")
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    ll2.insert("9")
    ll2.insert("5")
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> None"


def test_merge_lists_empty_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ } -> None"

def test_merge_lists_first_list_empty():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll2.insert("4")
    ll2.insert("9")
    ll2.insert("5")
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ 5 } -> { 9 } -> { 4 } -> None"

def test_merge_lists_second_list_empty():
    ll1 = LinkedList()
    ll1.insert("3")
    ll1.insert("1")
    ll2 = LinkedList()
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ 1 } -> { 3 } -> None"

def test_merge_lists_different_lengths():
    ll1 = LinkedList()
    ll1.insert("2")
    ll1.insert("1")
    ll2 = LinkedList()
    ll2.insert("9")
    ll2.insert("5")
    ll2.insert("4")
    ll2.insert("3")
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ 1 } -> { 3 } -> { 2 } -> { 4 } -> { 5 } -> { 9 } -> None"

def test_merge_lists_same_values():
    ll1 = LinkedList()
    ll1.insert("2")
    ll1.insert("2")
    ll1.insert("2")
    ll2 = LinkedList()
    ll2.insert("2")
    ll2.insert("2")
    ll2.insert("2")
    ll3 = LinkedList().merge_lists(ll1, ll2)
    assert ll3.to_string() == "{ 2 } -> { 2 } -> { 2 } -> { 2 } -> { 2 } -> { 2 } -> None"
