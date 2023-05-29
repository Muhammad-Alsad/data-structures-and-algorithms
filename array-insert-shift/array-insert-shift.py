

def insertShiftArray(arr, val):
    """
    This function takes in an array and a value to be added, and returns a new array with the value added at the middle index.
    """
    mid = len(arr) // 2 
    new_Arr = []  
    
    for i in range(len(arr)):
        if i == mid:
            new_Arr.append(val) 
        new_Arr.append(arr[i])  
        
    return new_Arr



arr = [1, 2, 3, 4, 5]
val = 10
new_Arr = insertShiftArray(arr, val)
print(new_Arr)  # Output: [1, 2, 3, 10, 4, 5]



arr = [1, 2, 3, 4]
val = 10
new_Arr = insertShiftArray(arr, val)
print(new_Arr)  # Output: [1, 2, 10, 3, 4]