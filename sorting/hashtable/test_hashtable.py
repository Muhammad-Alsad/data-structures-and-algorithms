import pytest 
from hashtable import (HashTable,TreeNode,BinaryTree,tree_intersection)

hash = HashTable()


def test_hash_method():
    hash = HashTable()
    actual = hash._HashTable__hash('d')
    assert 100 == actual

def test_set_method():
    hash = HashTable()
    hash.set("H","HI")
    assert hash.get("H") == "HI"

def test_get_method():
    hash = HashTable()
    hash.set("A","HI")
    hash.set("B","how are you")
    assert hash.get("B") == "how are you"

def test_has_method():
    hash = HashTable()
    hash.set("A","red")
    hash.set("B","blue")
    assert hash.has("C") == False

def test_return_none_for_no_existing_key():
    hash = HashTable()
    hash.set("1","Red")
    assert hash.get("1") == "Red"
    assert hash.get("2") == None

def test_all_keys():
    hash = HashTable()
    hash.set("1","Red")
    hash.set("A","Red")
    hash.set("#","Red")
    assert hash.keys == ["1","A","#"]
    assert hash.keys != ["1","A","#","H","U"]

def test_collision_handling():
    hash = HashTable()
    hash.set("1","Red")
    assert hash.get("1") == "Red"
    hash.set("1","Blue")
    assert hash.get("1") == "Blue"
    hash.set("1","Orange")
    assert hash.get("1") == "Orange"


def test_hash_word1():
    hash = HashTable()
    expected = "a"
    actual = hash.repeated_word("Once upon a time, there was a brave princess who...")
    assert expected == actual
    
def test_hash_word2():
    expected = "summer"
    actual = hash.repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York...")
    assert expected == actual
  
def test_hash_word3():
    expected = "it"
    actual = hash.repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    assert expected == actual    





###### cc32

def test_tree_intersection_one():
    tree = BinaryTree()
    tree2 = BinaryTree()
    
    tree.root = TreeNode("10")
    tree.root.left = TreeNode("20")
    tree.root.right = TreeNode("50")
    tree.root.left.left = TreeNode("30")

    tree2.root = TreeNode("10")
    tree2.root.left = TreeNode("20")
    tree2.root.right = TreeNode("50")
    tree2.root.left.left = TreeNode("30")
    tree2.root.left.right = TreeNode("40")
    tree2.root.left.right.left = TreeNode("70")
    
    assert  tree_intersection(tree,tree2) == ['30', '20', '10', '50']

def test_tree_intersection_two():
    tree = BinaryTree()
    tree2 = BinaryTree()
    
    tree.root = TreeNode("150")
    tree.root.left = TreeNode("100")
    tree.root.right = TreeNode("250")
    tree.root.left.left = TreeNode("75")
    tree.root.left.right = TreeNode("160")
    tree.root.left.right.left = TreeNode("125")
    tree.root.left.right.right = TreeNode("175")
    tree.root.right.left = TreeNode("200")
    tree.root.right.right = TreeNode("350")
    tree.root.right.right.left = TreeNode("300")
    tree.root.right.right.right = TreeNode("500")
    
    tree2.root = TreeNode("42")
    tree2.root.left = TreeNode("100")
    tree2.root.right = TreeNode("600")
    tree2.root.left.left = TreeNode("15")
    tree2.root.left.right = TreeNode("160")
    tree2.root.left.right.left = TreeNode("125")
    tree2.root.left.right.right = TreeNode("175")
    tree2.root.right.left = TreeNode("200")
    tree2.root.right.right = TreeNode("350")
    tree2.root.right.right.left = TreeNode("4")
    tree2.root.right.right.right = TreeNode("500")
    
    assert  tree_intersection(tree,tree2) == ["100","125","160","175","200","350","500"]
                                            

def test_tree_intersection_three():
    tree = BinaryTree()
    tree2 = BinaryTree()
    
    tree.root = TreeNode("A")
    tree.root.left = TreeNode("B")
    tree.root.right = TreeNode("C")
    tree.root.left.left = TreeNode("D")
    tree.root.left.right = TreeNode("E")
    tree.root.right.left = TreeNode("F")
    
    tree2.root = TreeNode("A")
    tree2.root.left = TreeNode("B")
    tree2.root.right = TreeNode("D")
    tree2.root.left.left = TreeNode("X")
    tree2.root.left.right = TreeNode("E")
    tree2.root.right.left = TreeNode("F")
    tree2.root.right.left.left = TreeNode("L")
    
    assert  tree_intersection(tree,tree2) == ['B', 'E', 'A', 'F', 'D']