import pytest 

from hashtable import HashTable

def test_hash_method():
    hash = HashTable()
    actual = hash._HashTable__hash('d')
    assert 652 == actual

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