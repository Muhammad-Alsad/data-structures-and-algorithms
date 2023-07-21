#  Merge Sort 

## Author : Muhammad Al-sad

### Testing :
    - Pytest

### How to run the tests?
    - cd to the file 
    - pytest tests.py



### Algorithms
    - def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


### Test cases visualization :
  Case 1:

    - input : [8,4,23,41,16,15]
    - output : [4,8,15,16,23,41]


  Case 2:
  - Input : [20,18,12,8,4,-2]
  - splitting : [20,18,12],[8,5,-2]
  - splitting : [20],[18],[12],[8],[5],[-2]
  - merging  : [18,20],[12],[5,8],[-2]
  - merging  : [12,18,20],[-2,5,8]
  - merging  : [-2,5,8,12,18,20]
  - Result : [-2,5,8,12,18,20] 


## Efficecncy : 
    - Time O(n log n)
    - space : O(n) 