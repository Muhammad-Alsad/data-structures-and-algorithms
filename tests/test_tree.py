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




def test_tree_istantiation():
    tree = Tree()
    assert tree.root == None


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




def test_find_maximum_value():
    # Test Case 1: Tree with a single node
    tree1 = BinarySearch()
    tree1.add(5)
    assert tree1.find_maximum_value() == 5

    # Test Case 2: Tree with multiple nodes
    tree2 = BinarySearch()
    tree2.add(2)
    tree2.add(7)
    tree2.add(3)
    tree2.add(1)
    tree2.add(6)
    tree2.add(9)
    tree2.add(4)
    assert tree2.find_maximum_value() == 9

    # Test Case 3: Tree with negative values
    tree3 = BinarySearch()
    tree3.add(-10)
    tree3.add(-5)
    tree3.add(-15)
    tree3.add(-20)
    tree3.add(-3)
    tree3.add(-7)
    tree3.add(-2)
    assert tree3.find_maximum_value() == -2

    # Test Case 4: Tree with a single branch
    tree4 = BinarySearch()
    tree4.add(1)
    tree4.add(2)
    tree4.add(3)
    tree4.add(4)
    assert tree4.find_maximum_value() == 4

    # Test Case 5: Tree with all identical values
    tree5 = BinarySearch()
    tree5.add(8)
    tree5.add(8)
    tree5.add(8)
    assert tree5.find_maximum_value() == 8

    # Test Case 6: Tree with a mix of positive and negative values
    tree6 = BinarySearch()
    tree6.add(4)
    tree6.add(-2)
    tree6.add(-5)
    tree6.add(0)
    tree6.add(7)
    tree6.add(3)
    tree6.add(-8)
    assert tree6.find_maximum_value() == 7

    # Test Case 7: Tree with only negative values
    tree7 = BinarySearch()
    tree7.add(-10)
    tree7.add(-15)
    tree7.add(-20)
    tree7.add(-12)
    tree7.add(-7)
    tree7.add(-9)
    assert tree7.find_maximum_value() == -7

    # Test Case 8: Empty tree
    tree8 = BinarySearch()
    assert tree8.find_maximum_value() == float('-inf')