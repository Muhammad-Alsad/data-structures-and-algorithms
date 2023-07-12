from insertion import insert, insertion_sort


def test_insert():
    sorted_array = [1, 4, 5, 9]
    value = 12
    insert(sorted_array, value)
    assert sorted_array == [1, 4,  5, 9, 12]


def test_insertion_sort():
    input_array = [5, 2, 4, 6, 1, 3]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == [1, 2, 3, 4, 5, 6]

def test_insertion_sort_single_element_input():
    input_array = [3]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == [3]

def test_insert_empty_sorted():
    sorted_array = []
    value = 4
    insert(sorted_array, value)
    assert sorted_array == [4]


