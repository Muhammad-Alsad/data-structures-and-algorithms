
arr = [1, 2, 3, 4, 5,7,8,9,89,90]
arr1=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199] 

def reverse_array(arr):
    
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr[i])
    
    reversed_arr = []
    while newArr:
        reversed_arr.append(newArr.pop())
    return reversed_arr


print(reverse_array(arr))
print(reverse_array(arr1))
