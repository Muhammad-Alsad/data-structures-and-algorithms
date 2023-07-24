import pytest 
from hashtable import HashTable

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