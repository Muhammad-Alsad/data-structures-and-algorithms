from merge_sort import merge_sort
    
def test_merge_sort_empty_list():
    arr = []
    merge_sort(arr)
    assert arr == []

def test_merge_sort_single_element():
    arr = [5]
    merge_sort(arr)
    assert arr == [5]

def test_merge_sort_sorted_array():
    arr = [1, 2, 3, 4, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_merge_sort_reversed_array():
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_merge_sort_random_array():
    arr = [8, 4, 23, 42, 16, 15]
    merge_sort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_Reverse_sorted():
    arr = [20,18,12,8,5,-2]
    merge_sort(arr)
    assert arr == [-2,5,8,12,18,20]    


def test_Nearly_sorted():
    arr = [2,3,5,7,13,11]
    merge_sort(arr)
    assert arr == [2,3,5,7,11,13]    

    

