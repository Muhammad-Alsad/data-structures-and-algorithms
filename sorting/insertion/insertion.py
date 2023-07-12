def insert(sorted_array, value):
    i = 0
    while i < len(sorted_array) and value > sorted_array[i]:
        i += 1
    sorted_array.insert(i, value)


def insertion_sort(input):
    sorted = []
    sorted.append(input[0])
    for i in range(1, len(input)):
        insert(sorted, input[i])
    return sorted