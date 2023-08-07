import pytest
from hashtableleftjoin import HashTable,left_join

def test_left_join_empty_hashmaps():
    hash_synonyms = HashTable()
    hash_antonyms = HashTable()

    result = left_join(hash_synonyms, hash_antonyms)

    assert result == []

def test_left_join_one_empty_hashmap():
    hash_colors = HashTable()
    hash_fruits = HashTable()

    hash_colors.set('red', 'apple')
    hash_colors.set('yellow', 'banana')
    hash_colors.set('green', 'pear')

    result = left_join(hash_colors, hash_fruits)

    expected_result = [['red', 'apple', None], ['yellow', 'banana', None], ['green', 'pear', None]]
    assert result == expected_result



def test_left_join_hashmap():
    hash_colors = HashTable()
    hash_fruits = HashTable()

    hash_colors.set('red', 'apple')
    hash_colors.set('yellow', 'banana')
    hash_colors.set('green', 'pear')

    result = left_join(hash_colors, hash_fruits)  # Call the left_join function

    expected_result = [['red', 'apple', None], ['yellow', 'banana', None], ['green', 'pear', None]]
    assert result == expected_result

def test_left_join_duplicate_keys():
    hash_partners1 = HashTable()
    hash_partners2 = HashTable()

    hash_partners1.set('Alice', 'Bob')
    hash_partners1.set('Eve', 'John')

    hash_partners2.set('Eve', 'Michael')
    hash_partners2.set('Mia', 'Daniel')

    result = left_join(hash_partners1, hash_partners2)

    expected_result = [['Alice', 'Bob', None], ['Eve', 'John', 'Michael']]
    assert result == expected_result
