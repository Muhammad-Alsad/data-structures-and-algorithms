import pytest
from trees.tree import (
    Tree,
    BinarySearch,
    Tnode
    )


def test_tree_istantiation():
    tree = Tree()
    assert tree.root == None

# @pytest.mark.skip(reason="Done")
def test_single_root_tree_istantiation():
    tree = BinarySearch()
    tree.add(11)
    assert tree.root.value == 11

def test_binary_tree_left_and_right_addition():
    tree = BinarySearch()
    tree.add(10)
    tree.add(15)
    tree.add(5)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15
    
def test_tree_Depths_first():
    tree = Tree()
    
    tree.root = Tnode("A")
    tree.root.left = Tnode("B")
    tree.root.right = Tnode("C")
    tree.root.left.left = Tnode("D")
    tree.root.left.right = Tnode("E")
    tree.root.right.left = Tnode("F")

    assert tree.pre_order() == ['A', 'B', 'D', 'E', 'C', 'F']
    assert tree.in_order() == ['D', 'B', 'E', 'A', 'F', 'C']
    assert tree.post_order() == ['D', 'E', 'B', 'F', 'C', 'A']

def test_binary_tree_contains():
    tree = BinarySearch()
    tree.add(23)
    tree.add(8)
    tree.add(42)
    tree.add(27)
    tree.add(85)
    tree.add(105)
    tree.add(4)
    tree.add(16)
    tree.add(15)
    tree.add(12)
    
    assert tree.contains(23) == True
    assert tree.contains(4) == True
    assert tree.contains(16) == True
    assert tree.contains(105) == True
    assert tree.contains(12) == True
    assert tree.contains(7) == False
    assert tree.contains(0) == False
    assert tree.contains(200) == False